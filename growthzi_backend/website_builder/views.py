from rest_framework import generics, status
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import RegisterSerializer, LoginSerializer,WebsiteSerializer
from rest_framework.permissions import IsAuthenticated
from .models import User
import uuid
import json
from rest_framework.response import Response
from rest_framework.views import APIView
import cohere
from .models import Website
from django.shortcuts import render, get_object_or_404

def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)
    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }

class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            tokens = get_tokens_for_user(user)
            return Response({"user": serializer.data, "tokens": tokens}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data
            tokens = get_tokens_for_user(user)
            return Response({"tokens": tokens}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class GenerateWebsiteView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        business_type = request.data.get('business_type')
        industry = request.data.get('industry')

        co = cohere.Client("tIW3CFfrt37DAHSXASE7fb0sqYQSFkofv0gKaGRy")  # Replace with your actual key

        # Ask for a clean JSON response
        prompt = f"""
Create website content for a {business_type} in the {industry} industry.
Return the result as a JSON object in this format:

{{
  "hero_text": "<one-line hero message>",
  "about": "<3–5 sentence about section>",
  "services": ["service 1", "service 2", "service 3", ...]
}}

Only return valid JSON. Do not include any explanation.
"""

        response = co.chat(
            model="command-r-plus",
            message=prompt
        )

        try:
            content = json.loads(response.text)
        except json.JSONDecodeError:
            return Response({"error": "Invalid response from language model."}, status=500)

        # Create Website object
        website = Website.objects.create(
            user=request.user,
            name=f"{business_type} Website",
            business_type=business_type,
            industry=industry,
            preview_id=uuid.uuid4(),
            content=content
        )

        serializer = WebsiteSerializer(website)
        return Response(serializer.data)

class WebsiteListView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = WebsiteSerializer

    def get_queryset(self):
        return Website.objects.filter(user=self.request.user)

class WebsiteDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = WebsiteSerializer

    def get_queryset(self):
        return Website.objects.filter(user=self.request.user)

def preview_website(request, preview_id):
    website = get_object_or_404(Website, preview_id=preview_id)
    content = website.content

    return render(request, "preview_template.html", {
        "name": website.name,
        "hero_text": content.get("hero_text", ""),
        "about": content.get("about", ""),
        "services": content.get("services", []),
    })





