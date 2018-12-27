from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post,Comments
from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView
from rest_framework.authentication import SessionAuthentication,BasicAuthentication
from rest_framework.response import Response


class CsrfExemptSessionAuthentication(SessionAuthentication):

    def enforce_csrf(self, request):
        return


@csrf_exempt
def post_list(request):
	posts = Post.objects.all()
	return render(request, 'blog/post_list.html', {'posts': posts})

@csrf_exempt
def post_list_num(request, pk):
    posts = get_object_or_404(Post, pk=pk)
    comment = Comments.objects.filter(ids=pk)
    return render(request, 'blog/post_list_num.html', {'posts': posts,'comments': comment,'upvotes':0})



class add_comment(APIView):

    authentication_classes = (
        CsrfExemptSessionAuthentication, BasicAuthentication)

    def post(self, request, *args, **kwargs):
        response = {}
        response['status'] = 500
        try:
            data = request.data
            comment = data['comment']
            pk = data['pk']
            temp = Comments.objects.create(comment = comment, ids = pk)
            response['status'] = 200
            response['comment'] = comment
        except Exception as e:
            print("Error PostContentAPI", str(e))

        return Response(data=response)

class new_vote(APIView):

    authentication_classes = (
        CsrfExemptSessionAuthentication, BasicAuthentication)

    def post(self, request, *args, **kwargs):

        response = {}
        response['status'] = 500
        data = request.data
        try:
            blog = Post.objects.get(pk = data['pk']);
            blog.votes += 1
            blog.save()
            response['votes'] = blog.votes


        except Exception as e:
            print("Error PostContentAPI", str(e))

        return Response(data=response)

AddComment = add_comment.as_view()
upvote = new_vote.as_view()