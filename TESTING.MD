# **The Recipe Hotspot Testing**

The site has been tested on various browsers across PC, mobile and tablet and works across all devices.

## **Manual Testing**

### **Test: Load add recipe form**

* **Expected outcome:** The add recipe form loads.
* **Actual Outcome:** When clicking on button to add recipe there is a 404 page note found error, stating that "No recipe matches the given query", and was being raised by the Recipe Detail view.
* **Solution:** In the urls.py file I changed the order the paths were listed in/ I moved the **add recipe** path above the **recipe detail** path.
* **Retest outcome:** Clicking on add recipe now loads the add recipe form and the user is now able to add a recipe.

### **Test: Required fields and correct field types on Recipe form**
* **Expected Outcome:** Required fields provide errors for missing data and number fields only accepts numbers.
* **Actual Outcome:** Any attempt to add incorrect data or required fields that are left blank cause an error message stating what the user needs to do to complete the form.

### **Test: Add recipe**
* **Expected outcome:** The ability to add a recipe to the site with either an uploaded image or a placeholder image if the user does not upload an image.
* **Actual Outcome:** Recipe is added successfully but only with placeholder images regardless of whether an image is submitted on the form.
* **Solution:** Add request.files to form parameters so that the form collects the uploaded image.
* **Retest Outcome:** When uploading recipes the uploaded image is displayed if it has been added to the form.

### **Test: Edit Recipe**
* **Expected outcome:** If the current website user is the author of the recipe they are viewing, they have the ability to load the recipe form and edit the recipe.
* **Actual Outcome:** The recipe form loads and users can fill it in and submit the updated recipe.

### **Test: Delete Recipe**
* **Expected Outcome:** If the current website user is the author of the recipe they are viewing, they have the ability to delete the recipe.
* **Actual Outcome:** The recipe is deleted and users are redirected to the homepage.

### **Test: Add Comment**
* **Expected Outcome:** On the recipe detail a registered user can add comments to a recipe and engage with other users.
* **Actual Outcome:** Registered users are able to use the add comment form and add their comments.

### **Test: Delete Comment**
* **Expected Outcome:** Users have the ability to delete their own comments on a recipe.
* **Actual Outcome:**

### **Test: Access to add recipe page restricted to registered users**
* **Expected Outcome:** Unregistered users can not access the add recipe form.
* **Actual Outcome:** The navbar restricts access to the add recipe link using an authenticated user statement, but users can manually enter the web address and access the form.
* **Solution:** Add @loginRequired to the class view so that login is required to enter the page.
* **Retest Outcome:** The navbar still restricts access as before and manually entering the web address now redirects to the login page.

### **Test: 404 Errors**
* **Expected outcome:** Users are redirected to a 404 page if they enter an invalid address to the base web address.
* **Actual Outcome:** If users add invalid details to the web url then they are redirected to the 404 page.

## **Bugs**

**Edit/Delete Redirection**
When users edit a recipe or delete a comment they are redirected to the homepage instead of back to the recipe page they were viewing. I have been unable to find a soluttion to this at present, but it is something I will try to find and resolve at a later date.

**Created/Updated Date**
When recipes are created, they are given the current date and time automatically as per the database model fields. If a recipe is updated however, the new created date is given. This changes the order the recipes are displayed on the homepage. I have an 'updated_on' field to cover this but need to figure out a way to lock in  the original date in the 'created_on' field.