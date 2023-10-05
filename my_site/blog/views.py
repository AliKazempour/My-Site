from django.shortcuts import render
from datetime import date

posts = [
    {
        "slug": "the-chatbot",
        "image": "chatgpt.png",
        "author": "Ali Kazempour",
        "date": date(2022, 7, 21),
        "title": "ChatGPT",
        "exerpt": "ChatGPT, which stands for Chat Generative Pre-trained Transformer,is a large language model-based chatbot developed by OpenAI and launched on November 30, 2022, which enables users to refine and steer a conversation towards a desired length, format, style, level of detail, and language",
        "content": """
            Lorem ipsum dolor sit amet, consectetuer adipiscing elit, 
            sed diam nonummy nibh euismod tincidunt ut laoreet dolore magna aliquam erat

            Lorem ipsum dolor sit amet, consectetuer adipiscing elit, 
            sed diam nonummy nibh euismod tincidunt ut laoreet dolore magna aliquam erat

            Lorem ipsum dolor sit amet, consectetuer adipiscing elit, 
            sed diam nonummy nibh euismod tincidunt ut laoreet dolore magna aliquam erat
        """
    },
    {
        "slug": "hike-in-the-mountains",
        "image": "mountains.jpg",
        "author": "Maximilian",
        "date": date(2021, 7, 21),
        "title": "Mountain Hiking",
        "excerpt": "There's nothing like the views you get when hiking in the mountains! And I wasn't even prepared for what happened whilst I was enjoying the view!",
        "content": """
          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.
        """
    }
]


def starting_page(request):
    return render(request, "blog/start_page.html")


def post(request):
    return render(request, "blog/all_posts.html")


def post_detail(request, slug):
    return render(request, "blog/post-detail.html")
