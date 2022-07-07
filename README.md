# **The Recipe Hotspot**
[Deployed Site](https://the-recipe-hotspot.herokuapp.com/)

## **Aim of the Site**

The aim of the site is to allow users to share their favourite recipes with the site community and search for new recipes to try. Users will be able to like their favourite recipes and be involved in the conversation with the post owner by commenting on recipes. 

## **Planning stage**

I wanted the site to almost have a blog like feel with the UI displaying 2 rows of 3 recipes previews, which users are then able to click on to be taken to the full recipe detail view. I included meal type and meal tags in the recipe model to allow users to be able to search for these from a sidebar on the main page, although this feature is not currently live on the website and will be included in a future udpate to the site.  The meal types will be starter, main etc and the meal tags will include things such as what meat/fruits are in the meal, or even if the meal is gluten free.

## **Wireframes**

I created some wireframes as a rough planning guide for how I wanted the site to appear. These are below.

![Homepage Wireframe](/static/docs/images/homepage_wf.JPG)

![Recipe Detail](/static/docs/images/recipe_detail_wf.JPG)

![Add Recipe](/static/docs/images/add_recipe_wf.JPG)

![Comments](/static/docs/images/add_comment_wf.JPG)

## ** User Stories**

* As a **Site User** I can...
    * view a paginated list of recipes.
    * click on a recipe so that I can view it in full.
    * create an account so that I can interact with the site.
    * view comments that have been made about recipes so that I can view the conversation.
    * post comments on recipes so that I can be involved in the conversation.
    * post my own recipes so that I can share my recipes with the site user base.
    * like/unlike recipes so that I can interact with the content
    * view how many likes a recipe has so that I can see which recipes are most popular.

* As a **Site Admin** I can...
    * create, delete and update post so that I can manage the sites content.
    * delete comments so that I can ensure they’re appropriate.
    * delete user posted recipes so that I can ensure site posts are appropriate.

## **Database Models**

I created 2 database models for the website. A Recipe model for the recipes and a comments model for the comments feature

**Recipe Model**
* title = models.CharField(max_length=200, unique=True)
* slug = models.SlugField(max_length=200, unique=True)
* author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="recipes")
* created_on = models.DateTimeField(auto_now=True)
* featured_image = CloudinaryField("image", default="placeholder")
* excerpt = models.TextField(blank=True)
* ingredients = models.TextField()
* instructions = models.TextField()
* cooking_time = models.IntegerField()
* updated_on = models.DateTimeField(auto_now=True)
* meal_type = models.CharField(max_length=50)
* meal_tags = models.CharField(max_length=50)
* status = models.IntegerField(choices=STATUS, default=0)
* likes = models.ManyToManyField(User, related_name="recipe_likes", blank=True)

**Comments Model**
* models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name="comments")
* name = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_comments")
* body = models.TextField()
* created_on = models.DateTimeField(auto_now_add=True)
* updated_on = models.DateTimeField(auto_now_add=True)

## **Website Design**

### **The Recipe Hotspot Logo**

The sites log was designed by a childhood friend who I've know for about 30 years. He studied graphic design at college and although he doesn't work as a designer he has kept up his love for it as a hobby. I asked him to provide a logo for a recipe website with no specific colour palette in mind. As he knows me so well he designed the logo with my favourite colour combinations of red and black.

### **Colour Scheme**

The colour scheme of the website was dictated by the sites logo, made up of the colours black, white and red. The colours have a natural contrast which should lead to easy readability.

* Red #E01616
* Black #000000
* White #FFFFFC

![Colours](/static/docs/images/colours.JPG)

### **Navbar**

* The navbar is made using bootstrap classes to style and add responsiveness. It features the sites logo and various links. Different links are displayed dependent on if the current visitor is logged in or not. For smaller screens there is a navbar toggler to make navigation on smaller screens a pleasant experience.

![Navbar](/static/docs/images/navbar.JPG)

### **Homepage**

The homepage displays welcome message. The message displayed will depend on if the visitor is logged in or not. There is a 2 rows of 3 recipes cards, making 6 in total, which is the limit before the user will need to change page. The recipe cards display the title, image for recipe, an excerpt describing the recipe, author, creation date and how many likes it has.

### **Recipe Detail Page**

The recipe detail page opens when users click on a recipe. It displays the full recipe details, such as ingredients, instructions and cooking time. The image is also displayed and logged in users have ability to like/unlike the recipe and add or view comments.

### **Add recipe**

Registered users have the ability to add their own recipes. They do this using a form based on the recipe database model. Once they have submitted the form the recipe is added to the site for themselves and others to view.

### **Edit/delete recipe**

Registered users can also edit or delete their own posted recipes. There is an if statement in place to make sure that only the post creator can edit or delete their post. Admins/superusers can also delete other users posts but this can only be done through the admin panel.

### **Login/Logout/SignUp Pages**

The login, logout and signup pages use the standard bootstrap/django features. The header and footer have been extended to these pages giving them a customised feel and appearance in line with the rest of the site.


## **Future Features**

* **My recipes page**
    * A page where a user can view all the recipes they have uploaded to the site. This way they can easily find and update or delete their recipes.

* **Meal type/ meal tags sidebar**
    * A side bar which displays a list of meal types and tags that users can click on and be redirected to paginated view of the type or tag they clicked on. For example types include main, starters, dessert etc. Clicking on starters for example, displays all recipes with starter as the meal type.

* **Social Login**
    * Allowing users to use their google or facebook acounts to register to the site.

* **Hompage Recipe redirection**
    * Currently when adding a recipe, updating a recipe, or deleting a comment, users are redirected back to the homepage when the form is submitted. I would like to find a way to redirect them back to the recipe they just added or were originally viewing.

* **Search Feature**
    * Include a search feature in the sidebar so users can manually search for recipes.

* **Random Recipes**
    * Have a button users can click to be taken to a random recipe.

## **Technologies Used**

**Programming Languages**

* [HTML](https://en.wikipedia.org/wiki/HTML)
* [Python](https://www.python.org/)
* [CSS](https://en.wikipedia.org/wiki/CSS)
* [Javascript](https://www.javascript.com/)

**Supporting Frameworks and Technologies**

* [Django](https://www.djangoproject.com/) - The base of the project, used for logins, views, forms among other things.
* [Bootstrap](https://getbootstrap.com/) - used for website design and responsiveness.
* [Cloudinary](https://cloudinary.com/) - used for hosting all the images on the website.
* [Crispy Forms](https://django-crispy-forms.readthedocs.io/en/latest/) - used to format forms across the site.
* [Summernote](https://summernote.org/) - used for text input fields on the website to allow bullet points or numbered lists for fields like recipe instructions.

## **Testing and Bugs**

The details for the testing and bugs can be found here in [TESTING.md](TESTING.MD)

## **Credits**

### **Media**

* [Pixabay](https://pixabay.com/) - The placeholder image and image of the BBQ Ribs come from Pixaby. Images used on user recipes are all provided by the recipe uploader.
* [Google Fonts](https://fonts.google.com/) - This was used to import the Roboto and Caveat fonts used on the website.
* [Font Awesome](https://fontawesome.com/) - This was used for icons on across the site such as on buttons and the likes heart.
* [Kevin Edwards/Kreeeytivitee](https://www.instagram.com/kreeeytivitee/?hl=en) - My childhood friends of nearly 30 years who designed my websites logo.

### **Code**

I used various resources to overcome different parts of this project. These are listed below

* [Bootstrap Official Site](https://getbootstrap.com/)
* [Django Project Website](https://www.djangoproject.com/)
* [Codemy Youtube Channel](https://www.youtube.com/c/Codemycom)
* [Stack Overflow Website and Community](https://stackoverflow.com/)
* [Code Institute course program materials](https://codeinstitute.net/)

### **Other Acknowledgements**

* My wife Helen - My wife feels guilty for catching covid very close to my submission of this project, This meant I didn't have as much time as I would've like to dedicate to it, but that's nothing compared to the guilt I have over the many hours I've spent coding since starting the course but it will be worth it in the end.
* Richard Wells - My Code Institute mentor who always remains calm when faced with my panic of feeling like I'm not progressing and constant imposter syndrome.
* Various friends - Who encourage me on my journey and spent time testing my website for this project and uploaded recipes.