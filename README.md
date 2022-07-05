# **The Recipe Hotspot**

## **Aim of the Site**

The aim of the site is to allow users to share their favourite recipes with the site community and search for new recipes to try. Users will be able to like their favourite recipes and be involved in the conversation with the post owner by commenting on recipes. 

## **Planning stage**

I wanted the site to almost have a blog like feel with the UI displaying 2 rows of 3 recipes previews, which users are then able to click on to be taken to the full recipe detail view. I included meal type and meal tags in the recipe model to allow users to be able to search for these from a sidebar on the main page, although this feature is not currently live on the website and will be included in a future udpate to the site.  The meal types will be starter, main etc and the meal tags will include things such as what meat/fruits are in the meal, or even if the meal is gluten free.

## **Website Design**

### **The Recipe Hotspot Logo**

The sites log was designed by a childhood friend who I've know for about 30 years. He studied graphic design at college and although he doesn't work as a designer he has kept up his love for it as a hobby. I asked him to provide a logo for a recipe website with no specific colour palette in mind. As he knows me so well he designed the logo with my favourite colour combinations of red and black.

### **Colour Scheme**

The colour scheme of the website was dictated by the sites logo, made up of the colours black, white and red. The colours have a natural contrast which should lead to easy readability.

* Black #000
* Red #E01616
* White #FFFFFC

### **Navbar**

The navbar is made using bootstrap classes to style and add responsiveness. It features the sites logo and various links. Different links are displayed dependent on if the current visitor is logged in or not. For smaller screens there is a navbar toggler to make navigation on smaller screens a pleasant experience.

### **Homepage**

The homepage displays welcome message. The message displayed will depend on if the visitor is logged in or not. There is a 2 rows of 3 recipes cards, making 6 in total, which is the limit before the user will need to change page. The recipe cards display the title, image for recipe, an excerpt describing the recipe, author, creation date and how many likes it has.

### **Recipe Detail Page**

The recipe detail page opens when users click on a recipe. It displays the full recipe details, such as ingredients, instructions and cooking time. The image is also displayed and logged in users have ability to like/unlike the recipe and add or view comments.



## ** User Stories**

* As a **Site User** I can...
    * view a paginated list of recipes.
    * click on a recipe so that I can view it in full.
    * create an account so that I can interact with the site.
    * view comments that have been made about recipes so that I can view the conversation.
    * post comments on recipes so that I can be involved in the conversation.
    * post my own recipes so that I can share my recipes with the site user base.
    * view how many likes a recipe has so that I can see which recipes are most popular.

* As a **Site Admin** I can...
    * delete comments so that I can ensure they’re appropriate.
    * delete user posted recipes so that I can ensure site posts are appropriate.