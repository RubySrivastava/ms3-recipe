
<h1 align="center">Ruby's Kitchen</h1>
<h1 align="center"><img src="#" /></h1>

-[Live Website](http://ms3-recipe.herokuapp.com/home)

-[GitHub Repository](https://github.com/RubySrivastava/ms3-recipe)
 
 ## About

This project is made for food lovers who wants to try to cook himself and like to try different flavour.
This website is made with the personal experience of site owner who likes to cook and share his recipe so that others can also explore the recipe. 
For site owners it will be utility to increase their presence over the internet which lead to increase their business by adding more content by himself and others can also contribute by their recipe.
It is designed to be responsive on all devices and easy to navigate for users and owner.


## Table of Contents

[User Experience (UX)](#UX)

[Features](#features)

[Design](#design)

[Technologies Used](#technologies)

[Testing](#testing)

[Deployment](#deployment)

[Known Bugs](#bugs)

[Credits](#credits)

<a name="UX"></a>
## User Experience (UX)

### User Stories

This website gives the information about different recipe with cooking method posted by site owner and other users. 
Any food lover who wants to come and explore different taste then this website is perfect for him.
In this website he gets the information about different recipe based on category and can also post his recipe.
This site also provides to create your own account and post recipe.

- #### Generic Traveller
    1. I want to easily understand the purpose and the layout of the site without additional instructions needed.
    1. I want to intuitively navigate through the site to browse the content.
    1. I want the site is responsive on all device as I usually use phone for doing all such type of stuff.
    1. I want to be able to use the website on any device so I can keep it handy.
    1. I want to use the navigation at all times and have it readily available so I can quickly navigate from one page to another.

- ####  Admin/Site Owner
    1. As a site owner I want to read all the recipe.
    1. As a site owner I want to add, edit and delete my recipe.
    1. As a site owner I can delete others recipe from my site but can not edit whenever I want.
    1. As a site owner I want manage categories of recipes.I want to add, edit and delete the category.
    1. As a site owner I want to recieve the feedback of users.
    
- #### User who wants to get recipe
    1. I want to check the recipe without login or sign up on site.
    1. I want to get recipe by search option.
    1. I want to contact the site owner by sending message without login or sign up.
    1. I want to request the site owner for newsletter without login or sign up.

- #### User who wants to post recipe
    1. I want to create my profile by sign up.
    1. I want to easliy login and check my page.
    1. I want to add new recipe on my page and available to all users of site.
    1. I want to edit and delete my recipe only.
    1. I want to contact the site owner by sending simply message.
    1. I want to request for newsletter.
    
<a name="design"></a>     
## Design

### Colour 
      
- #### This website is design for food lovers who loves to eat and needs lots of motivation to cook.
    The main color which is used for header and footer is spring wood.
    
    <img src="static/color/spring-wood.png" height="40px" />
    
- #### The black, brown and white color is used for text-color and background-color for links and buttons which show intelligence and simplicity respectively.Because of this color the content looks simple and clear.
      
    <img src="static/color/black.png" height="40px" />
    <img src="static/color/brown.png" height="40px" />
    <img src="static/color/white.png" height="40px" />
      
### Typography

- #### The main font used is a cinzel with serif as a fallback font.
- #### The second font used is a Expo for brand name ,footer details and titles.

### Imagery

- #### 
    -[Image Optimizer](http://jpeg-optimizer.com/)

### Mockups

- #### Mockups were created using Adobe Xd.
    -[Desktop Wireframes](https://xd.adobe.com/view/08b0941d-7b49-4297-86cf-c7491db53f06-5de3/)
    
    -[Mobile Wireframes]()
- #### Mockup made through original website 
    -[Wireframes](https://techsini.com/multi-mockup/index.php)
    
    <img src="static/mockup/home.png" />
    <img src="static/mockup/login.png" />
    <img src="static/mockup/signup.png" />
    <img src="static/mockup/contact.png" />
    <img src="static/mockup/recipe.png" />
    
<a name="features"></a>
## Features

### Existing Features

- #### Common Features Across All Pages

    - Header allows user to easily navigate across all pages
      - The header itself is positioned to always be visible (positioned absolutely using Bootstrap 'fixed-top' class) at the top of the screen (mobile and desktop) which allows visitors to find it quickly.
      - The brand logo is positioned on the left and is visible on all pages.
      - Navigation is included in the header to let the user intuitively locate it.
      - Navigation links is more visible when hovered over. This lets the visitor know that it is clickable.
      - Navigation links collapse in a home menu when viewed on mobile device.
    
    - Accessibility
      - All Pages have a description in case the image link breaks as well as helps screen readers.
      - The home menu has aria-label added to let users with screen readers know where the toggleable menu is.
    
    - Buttons
      - All buttons are styled in the way to provide consistency across the page. 

    - Responsiveness
      - All Pages are responsive on different viewport size.

    - Footer
      - Footer has been designed to be at the bottom of the page, regardless of the amount of content. This aids the overall user experience.
      - All content has been spaced out and aligned to the center.
      - There are social links and when hovered over, it changed the color.

### Specific to Pages
- Home Page
    - This page has header, footer and search box. This page has also list of all recipe with name and image.The header has navigation bar and footer has copyright and social links.The image brings the user's attention and inviting the user to explore the website.

- Contact Page
    - This page contains a form where users can give feedback and ask questions. It has another form where users can request for newsletter by simply subscribe it. 

- Login Page 
    - This page has login form. After login user will reach on his page.

- Sign Up Page
    - This page has sign up form. After sign up a profile page created where users can add recipe.

- My Page 
    - This page consist of all recipes of respective user.

- Category Page
    - Only admin can access this page. In this page admin can manage categories.

- Recipe Description Page
    - This page displays recipe description of selected recipe.

### Future Features
  - Create a way for the user to rate the website without having to type up feedback.
  - A page where people can review the comments.


<a name="technologies"></a>
## Technologies Used

### Languages Used

  - [HTML5](https://en.wikipedia.org/wiki/HTML5)
  - [CSS3](https://en.wikipedia.org/wiki/Cascading_Style_Sheets)
  - [JavaScript](https://en.wikipedia.org/wiki/Javascript)
  - [Jquery](https://en.wikipedia.org/wiki/JQuery)
  - [Python](https://en.wikipedia.org/wiki/Python_(programming_language))

### Frameworks, Libraries and Programs Used

  - [Bootstrap v4.5.0](https://getbootstrap.com/) - Used for the responsive layout as well as custom components such as header, footer, images, icons, grids, cards, and collapse element.
  - [Font Awesome](https://fontawesome.com/) - Font Awesome is used to add social icons for socila links and icons for about us page.
  - [Google Fonts](https://fonts.google.com/) - Google Fonts is used to import 'Expo'
  - [Git](https://git-scm.com/) - Git is used to allow for tracking of any changes in the code and for the version control.
  - [GitPod](https://www.gitpod.io/) - GitPod, connected to GitHub, hosted the coding space and allowed the project to be committed to the Github repository.
  - [Github](https://github.com/) - GitHub is used to host the project files and publish the live website by using Git Pages.
  - [Heroku](https://www.heroku.com/) - Heroku is the cloud platform to deploying the app.
  - [Flask](https://flask.palletsprojects.com/en/1.1.x/) - Flask is the web framework for the app.
  - [Jinja](https://jinja.palletsprojects.com/en/2.11.x/) - Jinja is used for Python template.
  - [Werkzeug](https://werkzeug.palletsprojects.com/en/1.0.x/) - Werkzeug is used for password hashing and authentication and autohorization.
  - [Adobe Xd](https://www.adobe.com/ie/products/xd.html) - Adobe Xd is used to create mockups.
  

### Database

  - [MongoDB](https://www.mongodb.com/) - MongoDB is the fully managed cloud database service used for the project.
  
  
<a name="#testing"></a>
## Testing

### Functionality Testing
  - #### Navigation bar
     - The navigation bar stays at the top of the page on all screen sizes.
            - When the nav links clicks it opens the relevent page in same window with same header footer.
  - #### Footer
     - Footer is located at the bottom of the page regardless of the content amount.
     - When the social links are clicked, they open the relevant social media page in a new tab.
  
  - All external links is tested to make sure they open up the correct pages in new tabs.
  - All internal links is tested to make sure that all pages are correctly connected.
    
### CSS3 validator 
Validate by direct input 
    [CSS Validator](https://jigsaw.w3.org/css-validator/)
  - Test result : No Error Found But Warning

### HTML5 validator
Vaidate by direct input 
    [HTML5 Validator](https://validator.w3.org/#validate_by_input)
  - 

### JavaScript validator
Validate by direct input
    [JavaScript Validator](https://jshint.com/)
  - Test result : No Error Found But Warning

### Python Validator
    [Pyhton Validator](http://pep8online.com/)
  - Test result : Pass

### Usability Testing
  - This website is shared on slack channel to get the feedback.This is also shared with friends to check on different device and accessbility.

### Compatibility Testing
  - #### Browser Compatibility
    - Tested on Chrome, Firefox, Opera, Internet Explorer, Microsoft Edge, Safari.
  - #### OS Compatibility
    - Tested on iOS , Android 10 and Windows 10.
  - #### Tested for responsivness on [Chrome DevTools](https://developers.google.com/web/tools/chrome-devtools). 

### Performance Testing
  - #### Tested on Developer Tools Lighthouse.
    - To run a report

        1. Download Google Chrome for Desktop.
        2. In Google Chrome, go to the URL you want to audit. You can audit any URL on the web.
        3. Open Chrome DevTools.
        4. Click the Audits tab.
        5. To the left is the viewport of the page that will be audited. To the right is the Audits panel of Chrome DevTools, which is now powered by Lighthouse.
        6. Click Perform an audit. DevTools shows you a list of audit categories. Leave them all enabled.
        7. Click Run audit. After 30 to 60 seconds, Lighthouse gives you a report on the page.

  - #### A Lighthouse report in Chrome DevTools
    - Home Page Desktop and Mobile

     <img src="static/lighthouse/home-dt" height="120px"/>
     <img src="static/lighthouse/home-mb" height="120px"/>

    - Contact Page Desktop and Mobile

     <img src="static/lighthouse/contact-dt" height="120px"/>
     <img src="static/lighthouse/contact-mb" height="120px"/>

    - Login Page Desktop and Mobile

      <img src="static/lighthouse/login-dt.png" height="120px"/>
      <img src="static/lighthouse/login-mb" height="120px"/>

    - Signup Page Desktop and Mobile

      <img src="static/lighthouse/signup-dt" height="120px"/>
      <img src="static/lighthouse/signup-mb" height="120px"/>

    - My Page Desktop and Mobile

      <img src="static/lighthouse/mypage-dt" height="120px"/>
      <img src="static/lighthouse/mypage-mb" height="120px"/>

    - Recipe Description Page Desktop and Mobile

      <img src="static/lighthouse/recipe-dt" height="120px"/>
      <img src="static/lighthouse/recipe-mb" height="120px"/>

    - Manage Category Page Desktop and Mobile
   
      <img src="static/lighthouse/category-dt" height="120px" />
      <img src="static/lighthouse/category-mb" height="120px" />


### 
<a name="deployment"></a>
## Deployment

- ### 
<a name="credits"></a>
## Credits

### Code :

- Bootstrap library was used to create a responsive design. 
- 
### Content :

- All code was written by the Ruby Srivastava.

- To write up a README file the most helpful documents were
    - Code Institute [SampleREADME](https://github.com/Code-Institute-Solutions/SampleREADME)
    - Code Institute [README Template](https://github.com/Code-Institute-Solutions/readme-template)
    - [Markdown Cheatsheet](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet#code)
    
- To write up the content of page the most helpful site is
    - Recipe Page [Official Website](https://www.allrecipes.com/)
    

### Media :
- All images used were taken from [UnSplash website](https://unsplash.com/)

### Acknowledgements :

- I was inspired by the people of surrounding me who are foodie, loves cooking and love to try new recipe.
- Thanks to my fellow student and tutors on slack channel who helped me in some way.
- Thanks to my mentor Maranatha Ilesalnmi for helping me throughout the project and giving me important suggestions and feedback of my work.
 