from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from .models import Blog
from .serializers import BlogSerializer

class BlogListApiView(APIView):
    # add permission to check if user is authenticated
    permission_classes = [permissions.IsAuthenticated]

    # 1. List all
    def get(self, request, *args, **kwargs):
        blog_title = Blog.objects.filter(user = request.user.id)
        serializer = BlogSerializer(blog_title, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # 2. Create
    def post(self, request, *args, **kwargs):
        data = {
            'blog_title': request.data.get('task'), 
            'completed': request.data.get('completed'), 
            'user': request.user.id
        }
        return Response(data, status=status.HTTP_200_OK)


class BlogDetailApiView(APIView):
    # add permission to check if user is authenticated
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self, blog_id, user_id):
        '''
        Helper method to get the object with given blog_id, and user_id
        '''
        try:
            return Blog.objects.get(id=blog_id, user = user_id)
        except Blog.DoesNotExist:
            return None

       # 3. Retrieve
    def get(self, request, blog_id, *args, **kwargs):
        blog_instance = self.get_object(blog_id, request.user.id)
        if not blog_instance:
            return Response(
                {"res": "Object with blog id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = BlogSerializer(blog_instance)
        return Response(serializer.data, status=status.HTTP_200_OK)    

    # 4. Update
    def put(self, request, blogo_id, *args, **kwargs):
        blog_instance = self.get_object(blog_id, request.user.id)
        if not blog_instance:
            return Response(
                {"res": "Object with blog id does not exists"}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        data = {
            'blog_title': request.data.get('blog_title'), 
            'completed': request.data.get('completed'), 
            'user': request.user.id
        }
        serializer = BlogSerializer(instance = blog_instance, data=data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

     # 5. Delete
    def delete(self, request, blog_id, *args, **kwargs):
        blog_instance = self.get_object(blog_id, request.user.id)
        if not blog_instance:
            return Response(
                {"res": "Object with blog id does not exists"}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        blog_instance.delete()
        return Response(
            {"res": "Object deleted!"},
            status=status.HTTP_200_OK
        )    