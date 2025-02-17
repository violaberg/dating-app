![Image]()

# Love.exe – Coding Connections in the Digital Age 🌈!

# ***SparkSync***

## **Table of Contents**
* [**SparkSync**](#sparksync)
* [**About the Submission**](#about-the-submission)
    + [**Deployment**](#deployment)
    + [**Goal**](#goal)
    + [**Problem Statement**](#problem-statement)
    + [**Objective(s)**](#objectives)
    + [**Target Audience**](#target-audience)
* [**Pages**](#pages)
* [**Tech Stack**](#tech-stack)
    + [**Languages & Frameworks**](#languages--frameworks)
    + [**Database**](#database)
    + [**Authentication**](#authentication)
    + [**Styling & Fonts**](#styling--fonts)
    + [**Real-time Features**](#real-time-features)
    + [**Deployment & Services**](#deployment--services)
    + [**Development Tools**](#development-tools)
    + [**Additional Libraries**](#additional-libraries)
    + [**Email Provider**](#email-provider)
* [**Design**](#design)
    + [**Color Palette**](#color-palette)
    + [**Typography**](#typography)
* [**Future Development**](#future-development)
    + [**Enhanced Matching Algorithm**](#future-development)
    + [**Advanced Communication Features**](#advanced-communication-features)
    + [**Profile Enhancements**](#profile-enhancements)
    + [**Safety & Privacy**](#safety--privacy)
    + [**User Experience**](#user-experience)
    + [**Premium Features**](#premium-features)
    + [**Community Features**](#community-features)
* [**Credits**](#credits)
* [**Testing**](#testing)
* [**Team**](#team)

## **About the Submission**

### **Intro**
SparkSync is a modern dating application designed to help people form meaningful connections through shared interests, preferences, and compatibility matching. The platform emphasizes authentic interactions and provides a safe, engaging environment for users to meet potential partners.

### **Deployment**
[Deployed link](https://sparksync-7438f8dc8240.herokuapp.com/)

[Kanban board](https://github.com/users/violaberg/projects/12)

### **Goal**
The primary goal of SparkSync is to create a digital dating platform that excels in:

*   **Meaningful Connections:** Fostering genuine relationships, not just superficial interactions.
*   **User Safety:**  Prioritizing user safety through robust security measures and a trustworthy environment.
*   **Inclusivity:**  Creating a welcoming space for users of all backgrounds, genders, and sexual orientations.
*   **Accessibility:**  Providing a user-friendly and intuitive experience for everyone.


### **Problem Statement**
Traditional dating apps often fall short in several key areas:

*   **Superficiality:**  Overemphasis on physical appearance, leading to shallow connections.
*   **Safety Concerns:** Insufficient verification and safety protocols, exposing users to risks.
*   **Lack of Inclusivity:**  Not catering to the diverse needs and preferences of all users.
*   **Ineffective Matching:**  Poorly designed algorithms that result in mismatched connections and user dissatisfaction.
*   **Poor User Experience:** Confusing interfaces and difficult navigation, hindering the overall experience.



### **Objective(s)**

*   **Develop a robust matching algorithm:** Utilize user-provided data (questionnaire responses, preferences, and profile information) to connect individuals with high compatibility potential.
*   **Implement strong security features:** Include profile verification, reporting mechanisms, and data encryption to ensure user safety and data protection.
*   **Design an intuitive and accessible user interface:**  Create a clean, user-friendly design across all application pages that is accessible and enjoyable to use.
*   **Foster a welcoming and inclusive community:** Promote respectful interactions and provide a platform that is inclusive of all users, regardless of background, gender, or sexual orientation.
*   **Enable customizable and detailed user profiles:** Allow users to fully express their individuality and preferences through comprehensive profile fields.
*   **Provide multiple communication channels:** Offer a contact form for user inquiries and support, with a plan for future in-app chat functionality for matched users.

### **Target Audience**
SparkSync is designed for adults (18+) seeking various types of connections, including:

*   **Individuals Seeking Long-Term Relationships:** Those looking for committed, lasting partnerships.
*   **People Interested in Casual Dating:**  Users who want to meet new people and explore connections without immediate long-term commitments.
*   **Tech-Savvy Individuals:**  People comfortable using online platforms and apps for social interaction.
*   **Users Who Value Safety and Privacy:** Individuals who prioritize a secure and trustworthy online dating experience.
*   **Newcomers to Online Dating:**  The intuitive design makes it easy for those unfamiliar with online dating to get started.
* **Hopeless romantics:** Providing an experience that goes further than surface level.

## **Pages**

## **Tech Stack**

### **Languages & Frameworks**

- Python 3.11
- Django 5.1.6
- JavaScript
- HTML5
- CSS3

### **Database**

- PostgreSQL (via psycopg2-binary)
- [Neon database](https://console.neon.tech/)

### **Authentication**

- django-allauth (for user authentication)

### **Styling & Fonts**

- [Google Fonts](https://fonts.google.com)
- Bootstrap 5
- Crispy Forms with crispy-bootstrap5 for form styling

### **Real-time Features**

- Django Channels 4.2.0
- Daphne 4.1.2 (ASGI server)
- Redis (for WebSocket backing store)
- channels_redis 4.2.1

### **Deployment & Services**

- Heroku
- WhiteNoise 6.9.0 (static file serving)
- Cloudinary (if being used for image storage)

### **Development Tools**

- Git & GitHub for version control
- VS Code IDE
- python-dotenv for environment variable management

### **Additional Libraries**

- Pillow 11.1.0 (for image processing)
- django-notifications for user notification system

### **Email Provider**

- [Resend](https://resend.com/)

## **Design**

### **Color Palette**

Our color scheme combines deep, romantic burgundies with neutral tones to create an elegant and intimate atmosphere:

***Charcoal (#1b1b1b)***<br>
Used for main text providing strong contrast and readability.<br>

***Dark Burgundy (#2D0709)***<br>
Added to create depth and sophistication.<br>

***Red (#B10009)***<br>
Accent color for important elements.<br>

***Light Burgundy (#520408)***<br>
Used for hover states and secondary elements.<br>

***Pink (#fa9ca1)***<br>
Adds a soft, romantic touch to features.<br>

***Sea Salt (#fafafa)***<br>
Used for content areas requiring high brightness and clarity

***Cool Ivory (##F5F5EE)***<br>
Main background color, providing a slighty warmer, inviting atmosphere while being easier on the eyes

![Color palette](assets/colors/sparksync.png)

### **Typography**

The application uses a carefully selected dual-font system:

***Montserrat***<br>
A modern sans-serif font used for main content, navigation, and user interface elements. Its clean lines and excellent readability make it perfect for both headlines and body text.

![Montserrat font](assets/fonts/montserrat.png)

***Great Vibes***<br>
A romantic, script-style font used for logos and special headings. It adds an elegant, sophisticated touch that reinforces the dating app's romantic nature.

![Great vibes font](assets/fonts/great_vibes.png)

## **Future Development**

### **Enhanced Matching Algorithm**

- Implement AI-powered compatibility scoring
- Add personality quiz feature for better matches
- Develop interest-based group matching

### **Advanced Communication Features**

- Voice and video chat integration
- Message translation for international users
- Scheduled virtual date planning tool

### **Profile Enhancements**

- Video profile options
- Profile verification system
- Social media integration
- Interactive profile prompts and questions

### **Safety & Privacy**

- Advanced photo verification
- Block/report system enhancement
- Privacy settings customization
- Real-time inappropriate content detection

### **User Experience**

- Mobile app development
- Dark mode implementation
- Accessibility improvements
- Custom notification preferences

### **Premium Features**

- Subscription model implementation
- Priority matching
- Advanced filters
- Profile statistics and insights

### **Community Features**

-Interest-based forums
- Dating advice blog
- Success stories section
- Community events calendar

## **Credits**
- [Floating Love Heart Effect](https://codepen.io/1AHV/pen/oPvwQw)
- [Coolors color palette generator](https://coolors.co/)
- [Background pattern](https://devsnap.me/css-background-patterns?)
- [Hero Image](https://unsplash.com/photos/person-holding-fire-cracker-shallow-focus-photography-PAykYb-8Er8)
- [Favicon generator](https://favicon.io/favicon-converter/)
- [Favicon image](https://stock.adobe.com/ie/images/shiny-isolated-red-ruby-heart-shape-on-white-background/85233324?clickref=1100lA7oGHYg&mv=affiliate&mv2=pz&as_camptype=infinite-scroll-page-pricing_page_2025-ignore&as_channel=affiliate&as_source=partnerize&as_campaign=cheezy)

## **Testing**

Details of testing are included in a separate file [TESTING.md](TESTING.md).

## **Team**
- Viola Bergere - https://github.com/violaberg
- George Burn - https://github.com/Georgeburn94
- Jan Rafanan - https://github.com/yanidruffy
- Jaime Hyland - https://github.com/JaimeHyland
- Agnieszka Bialek - https://github.com/Agnieszka-21
- Evangelos Alexiou - https://github.com/Alexiou981
- Tamanna Islam - https://github.com/farhatamannaislam
