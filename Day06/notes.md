# Spring Boot Advanced & Security

## Step-8-Spring-Boot-Level-III-Scenario-Based
GenZ Career on YouTube
Subscribe for Interview Preparation
1) If you had to scale a Spring Boot application to handle high traffic, what strategies would you
use?
To scale a Spring Boot application for high traffic, we can:
• Add more app instances (horizontal scaling) and use a load balancer to spread out
the traffic.
• Break our app into microservices so each part can be scaled independently.
• Use cloud services that can automatically adjust resources based on our app's needs.
• Use caching to store frequently accessed data, reducing the need to fetch it from the
database every time.
• Implement an API Gateway to handle requests and take care of things like
authentication
2) Imagine Your application requires data from an external REST API to function. Describe how you
would use RestTemplate or WebClient to consume the REST API in your Spring Boot application.
Talking about RestTemplate:
First, I would define a RestTemplate bean in a configuration class using @Bean annotation so it can
be auto -injected anywhere I need it. Then, I'd use RestTemplate to make HTTP calls by creating an
instance and using methods like getForObject() for a GET r equest, providing the URL of the external
API and the class type for the response.
Talking about WebClient :
I would define a WebClient bean similarly using @Bean annotation. Then I would use this WebClient
to make asynchronous requests, calling methods like get(), specifying the URL, and then using
retrieve() to fetch the response. I would also handle the data u sing methods like bodyToMono() or
bodyToFlux() depending on if I am expecting a single object or a list.
3) Your Spring Boot backend needs to accept cross -origin requests from a specific frontend domain.
Explain how you would configure CORS policies in your application.
To enable cross -origin requests from a specific domain in Spring Boot, I would use the @CrossOrigin
annotation on my controller or method, like @CrossOrigin(origins = "http://example.com").
For a global approach, I'd configure a WebMvcConfigurer bean, overriding the addCorsMappings
method to apply rules across all controllers, using
registry.addMapping("/**").allowedOrigins("http://example.com").
This setup allows my backend to accept requests from a designated frontend domain and enhancing
security by restricting other cross -origin interactions.
4) Your Spring Boot application is experiencing performance issues under high load. What are the
steps you would take to identify and address the performance?
First, I would identify the specific performance issues using monitoring tools like Spring Boot
Actuator or Splunk.
GenZ Career on YouTube
Subscribe for Interview Preparation
I would also analyze application logs and metrics to spot any patterns or errors, especially under high
load.
Then, I would start a performance tests to replicate the issue and use a profiler for code -level
analysis.
After getting findings, I might optimize the database, implement caching, or use scaling options. It's
also crucial to continuously monitor the application to prevent future issues.
5) Imagine you need to make a simple web application with Spring Boot that serves a static
homepage and a dynamic page displaying current server time. Discuss the project structure you
would use.
I would add main application and a web controller in src/main/java directory and the controller
would have mappings for the homepage (@GetMapping("/")) and the server time page
(@GetMapping("/time"))
I would add Static content, like index.html in src/main/resources/static, while dynamic content uses
Thymeleaf templates in src/main/resources/templates.
Configuration settings would be there in src/main/resources/application.properties.
This setup efficiently organizes static and dynamic resources and ensuring clear separation and easy
management of web content.
6) Your application behaves differently in development and production environments. How would
you use Spring profiles to manage these differences?
To handle differences between development and production environments, I would use Spring
profiles.
By defining environment -specific configurations in application -dev.properties  for development and
application -prod.properties for production, I can easily switch behaviors based on the active profile.
Activating these profiles is simple, either by setting the spring.profiles.active property, using a
command -line argument, or through an environment variable.
Additionally, with the @Profile annotation, I would selectively load certain beans or configurations
according to the current environment and  ensuring that my application adapts seamlessly to both
development and production settings.
7) What strategies would you use to optimize the performance of a Spring Boot application?
Let’s say my Spring Boot application is taking too long to respond to user requests. I could:
• Implement caching for frequently accessed data.
• Optimize database queries to reduce the load on the database.
• Use asynchronous methods for operations like sending emails.
• Load Balancer if traffic is high
GenZ Career on YouTube
Subscribe for Interview Preparation
• Optimize the time complexity of the code
• Use webFlux to handle a large number of concurrent connections.
8) Describe a scenario where a Spring Boot application needs to dynamically switch between
multiple data sources at runtime based on the request context.
Imagine Spring Boot application that serves users from different places, like Europe or Asia, we
switch between databases based on where the user is from. This means if someone from Europe
visits the app, they get data from the European database, making th e content more relevant to them.
We set this up by having a special part in the app that knows which database to use when it sees
where the request is coming from. This way, users see information and offers that make sense for
their region.
9) Discuss how you would add a GraphQL API to an existing Spring Boot RESTful service.
First, I'd add GraphQL Java and GraphQL Spring Boot starter dependencies to my pom.xml or
build.gradle file. Secondly, I'd create a GraphQL schema file (schema.graphqls) in the
src/main/resources folder.
Then I'd data fetchers implement them to retrieve data from the existing services or directly from the
database and moving ahead, I'd configure a GraphQL service using the schema and data fetchers
Then I would expose the graphql endpoint and make sure it is correctly configured. Finally, I'd test
the GraphQL API using tools like GraphiQL or Postman to make sure it's working as expected
10) Describe how you would secure sensitive data in a Spring Boot application that is accessed by
multiple users with different roles.
To keep sensitive information safe in a Spring Boot app used by many people with different roles, I
would do a few things. First, I would make sure everyone who uses the app proves who they are
through a login system.
Then, I'd use special settings to control what each person can see or do in the app based on their role
like some can see more sensitive stuff while others can’t. I'd also scramble any secret information
stored in the app or sent over the internet so that only the right people can understand it.
Plus, I'd keep passwords and other secret keys out of the code and in a safe place, making them easy
to change if needed. Lastly, I'd keep track of who looks at or changes the sensitive information, just
to be  extra safe. This way, only the right people c an get to the sensitive data, and it stays protected
11) In an IoT application scenario, explain how a Spring Boot backend could be designed to
efficiently process and analyze real -time data streams from thousands of IoT devices.
In an IoT setup, a Spring Boot backend can manage data from lots of devices by using Apache Kafka,
a tool that helps collect all the data. It then processes this data in real -time, figuring out what's
important and what's not.
After sorting the data, it stores it in a database designed for quick access and analysis. This way, the
system can handle tons of information coming in all at once, making sure everything runs smoothly
and quickly.
GenZ Career on YouTube
Subscribe for Interview Preparation
12) Discuss the specific security challenges associated with using WebSockets in a Spring Boot
application.
WebSockets in Spring Boot apps face security issues because they keep a constant connection open
between the user and the server, unlike regular web pages.
This can lead to risks like attackers hijacking these connections to intercept or send fake messages.
Also, without the usual security checks we have for web pages, it's trickier to stop unauthorized
access.
To keep things safe, it's important to make sure only the right people can connect and to encrypt the
data being sent back and forth.
13) How would you implement efficient handling of large file uploads in a Spring Boot REST API,
ensuring that the system remains responsive and scalable?
To handle big file uploads in a Spring Boot REST API without slowing down the system, I'd use a
method that processes files in the background and streams them directly where they need to go, like
a hard drive or the cloud.
This way, the main part of the app stays fast and can handle more users or tasks at the same time.
Also, by saving files outside the main server, like on Amazon S3, it helps the app run smoothly even
as it grows or when lots of users are uploading files.
14) How you would use Spring WebFlux to consume data from an external service in a non -
blocking manner and process this data reactively within your Spring Boot application.
In a Spring Boot app using Spring WebFlux, I'd use WebClient to fetch data from an external service
without slowing things down. WebClient makes it easy to get data in a way that doesn't stop other
parts of the app from working.
When the data comes in, it's handled reactively, meaning I can work with it on the go like filtering or
changing it without waiting for everything to finish loading. This keeps the app fast and responsive,
even when dealing with a lot of data or making man y requests.
15) Imagine you need to develop a REST API in a Spring Boot application that allows clients to
manage user data. Explain how you would structure your application
To build a REST API in Spring Boot for managing user data, I'd organize the app into three main parts:
Controllers, Services, and Repositories. Controllers would deal with web requests, using endpoints
like /users to handle different actions —getting, addin g, updating, and deleting user info.
Services would focus on the app's logic, like checking if a user's data meets certain criteria before
saving it. Repositories would connect to the database to actually save, update, or fetch user data.
This setup keeps everything neat and makes it easier t o update parts of the app without affecting
others.
16) Imagine you are designing a Spring Boot application that interfaces with multiple external APIs.
How would you handle API rate limits and failures?
To handle API rate limits and failures in a Spring Boot application, I would
• Use a circuit breaker to manage failures
GenZ Career on YouTube
Subscribe for Interview Preparation
• Implement rate limiting to avoid exceeding API limits
• Add a retry mechanism with exponential backoff for temporary issues
• Use caching to reduce the number of requests.
This approach helps keep the application reliable and efficient
17) You need to deploy a Spring Boot application to a cloud platform (e.g., AWS, Azure). What
steps would you take, and how would you configure the application properties for different
environments
To deploy a Spring Boot app to the cloud, like AWS or Azure, first, I'd package it using Maven or
Gradle. Next, I'd pick a cloud service that makes deployment easy, such as AWS Elastic Beanstalk or
Azure App Service. For different settings in development, staging, and production, I'd use Spring
profiles.
I'd make separate property files for each environment, like application -dev.properties for
development. When deploying, I'd choose the right profile for that environment, making sure the
app uses the correct settings. This way, the app runs smoothly in any  environment with the right
configurations.
18) Explain how you would use application events in Spring Boot to notify different parts of your
application about significant activities
In Spring Boot, to let different parts of the app know about important activities, I'd use application
events. First, I'd create special event classes for different types of activities, like when a new user
signs up. Then, I'd write listeners for these eve nts, which are just pieces of code that wait for a
specific event to happen and then do something in response.
To tell the app when something important happens, I'd publish these events from anywhere in the
app. This way, parts of the app can communicate and react to events without being directly
connected, keeping the code clean and organized.
## Step-9-Spring-Security-Level-I
GenZ Career on YouTube
Subscribe for Interview Preparation
1) How does Spring Security integrate with OAuth2 for authorization
Spring Security integrates with OAuth2 for authorization by acting as a client that can request access
tokens from an OAuth2 provider.
It uses these tokens to authenticate and authorize users to access protected resources. When a user
tries to access a resource, Spring Security redirects them to the OAuth2 provider for login.
After successful authentication, the provider issues an access token to Spring Security, which it then
uses to verify the user's permissions and grant access to the resource. This integration enables
seamless and secure access control in applications.
2) Explain Cross -Origin Resource Sharing (CORS) and how you would configure it in a Spring Boot
application.
Cross -Origin Resource Sharing  allows a website to safely access resources from another website. In
Spring Boot, we can set up CORS by adding @CrossOrigin to controllers or by configuring it globally.
This tells our application which other websites can use its resources, what type of requests they can
make, and what headers they can use.
This way, We control who can interact with our application, keeping it secure while letting it
communicate across different web domains.
3) Explain SecurityContext and SecurityContext Holder in Spring security.
In Spring Security, the SecurityContext is where details about the currently authenticated user are
stored, like user details and granted authorities.
The SecurityContextHolder is a helper class that holds the SecurityContext. It's like a container or
storage space that keeps track of the authentication information of the current user throughout the
application.
This makes it easy to access the user's details anywhere in the application, ensuring that security
decisions can be made based on the user's authentication status and roles.
4) What do you mean by OAuth2 Authorization code grant type
The OAuth2 Authorization Code grant type is a secure way to authenticate and authorize users. It
works by directing the user to a login page managed by the OAuth2 provider (like Google or
Facebook).
After logging in, the user is given a code.
This code is then exchanged for an access token by the application's backend server. This access
token is used to access the user's data securely.
This process keeps user credentials safe, as the actual token exchange happens away from the user's
device, minimizing the risk of sensitive information being exposed.
5) How does Spring Security protect against Cross -Site Request Forgery (CSRF) attacks, and under
what circumstances might you disable CSRF protection?
Spring Security protects against CSRF attacks by generating unique tokens for each session and
requiring that each request from the client includes this token.
GenZ Career on YouTube
Subscribe for Interview Preparation
This ensures the request is from the authenticated user, not a malicious site. However, CSRF
protection might be disabled for APIs meant to be accessed by non -browser clients, like mobile apps
or other back -end services, where the risk of CSRF is low and t okens can't be easily managed.
Disabling CSRF in these cases simplifies the integration with these services without significantly
compromising security.
6) How can you implement method -level security in a Spring application, and what are the
advantages of this approach?
To implement method -level security in a Spring application, I can use annotations like @PreAuthorize
or @Secured on individual methods. These annotations check if the user has the required
permissions or roles before executing the method.
The advantage of this approach is that it provides fine -grained control over who can access specific
functionalities within the application. This means I can restrict sensitive operations at the method
level, ensuring that only authorized users can perform  certain actions, which enhances the overall
security of the application.
7) Your organization uses an API Gateway to route requests to various microservices. How would
you leverage Spring Security to authenticate and authorize requests at the gateway level before
forwarding them to downstream services?
At the API Gateway, I can use Spring Security to check if requests are allowed before sending them to
other services.
By checking tokens or using OAuth2 at the gateway, I make sure only valid and authorized requests
get through.
This means each service doesn't have to check security separately, making the whole system simpler
and safer.
8) How can you use Spring Expression Language (SpEL) for finegrained access control?
I can use Spring Expression Language (SpEL) for fine -grained access control by embedding it in
security annotations like @PreAuthorize. For example, I can write expressions that check if a user has
specific roles, and permissions, or even match against met hod parameters to decide access.
This allows for very detailed and flexible security rules directly in the code, letting me tailor access
rights precisely to the user's context and the operation being performed. Using SpEL in this way helps
in creating dynamic and complex security conditi ons without cluttering the business logic.
9) In your application, there are two types of users: ADMIN and USER. Each type should have
access to different sets of API endpoints. Explain how you would configure Spring Security to
enforce these access controls based on the user's role.
In the application, to control who can access which API endpoints, I can use Spring Security to set
rules based on user roles. I can configure it so that only ADMIN users can reach adminrelated
endpoints and USER users can access user -related endpoints.
This is done by defining patterns in the security settings, where I link certain URL paths with specific
roles, like making all paths starting with "/admin" accessible only to users with the ADMIN role, and
paths starting with "/user" accessible to those w ith the USER role. This way, each type of user gets
access to the right parts of the application.
GenZ Career on YouTube
Subscribe for Interview Preparation
10) What do you mean by digest authentication?
Digest authentication is a way to check who is trying to access something online without sending
their actual password over the internet. Instead, it sends a hashed (scrambled) version of the
password along with some other information.
When the server gets this scrambled password, it compares it with its own scrambled version. If they
match, it means the user's identity is verified, and access is granted. This method is more secure
because the real password is never exposed during the ch eck.
11) What is the best practice for storing passwords in a Spring Security application?
The best practice for storing passwords in a Spring Security application is to never store plaintext
passwords. Instead, passwords should be hashed using a strong, one -way hashing algorithm like
bcrypt, which Spring Security supports.
Hashing converts the password into a unique, fixed -size string that cannot be easily reversed.
Additionally, using a salt (a random value added to the password before hashing) makes the hash
even more secure by preventing attacks like rainbow table lookups . This way, even if the password
data is compromised, the actual passwords remain protected.
12) Explain the purpose of the Spring Security filter chain and How would you add or customize a
filter within the Spring Security filter chain
The Spring Security filter chain is a series of filters that handle authentication and authorization in a
Spring application. Each filter has a specific task, like checking login credentials or verifying if a user
has access to certain resources.
To add or customize a filter, I can define a new filter class and add it to the filter chain in the security
configuration. This is done by using the addFilterBefore, addFilterAfter, or addFilterAt methods,
specifying where in the chain the new filter shou ld be placed, to ensure it's executed at the correct
point during the security processing.
13) How does Spring Security handle session management, and what are the options for handling
concurrent sessions
Spring Security handles session management by creating a session for the user upon successful
authentication. For managing concurrent sessions, it provides options to control how many sessions
a user can have at once and what happens when the limit is exce eded.
For example, I can configure it to prevent new logins if the user already has an active session or to
end the oldest session. This is managed through the session management settings in the Spring
Security configuration, where I can set policies like maximu mSessions to limit the number of
concurrent sessions per user.
14) You've encountered an issue where users are being unexpectedly denied access to a resource
they should have access to. Describe your approach to debugging this issue in a Spring Security -
enabled application.
To debug access issues in a Spring Security -enabled application, I would start by checking the security
configuration to ensure the correct roles and permissions are set for the resource. Next, I would
examine the logs to see if Spring Security is throwing  any specific errors or denying access for a
particular reason.
GenZ Career on YouTube
Subscribe for Interview Preparation
I might also enable debug logging for Spring Security to get more detailed information about the
security decisions being made. Additionally, verifying the user's assigned roles and the methodlevel
security annotations, if any, would help identify if the a ccess rules are correctly applied.
15) Describe how to implement dynamic access -control policies in Spring Security.
To implement dynamic access -control policies in Spring Security, We can use the Spring Expression
Language (SpEL) within the @PreAuthorize or @PostAuthorize annotations to define complex,
runtime -evaluated conditions for access control.
This allows the access rules to be determined based on the current state of the application, user
properties, or method parameters. For example, by fetching roles or permissions from a database at
runtime, we can dynamically decide whether a user can acces s a specific method or resource,
allowing for more flexible and context -sensitive security policies.
16) How do you test security configurations in Spring applications?
To test security configurations in Spring applications, I use Spring Security's testing support, which
includes annotations like @WithMockUser or @WithAnonymousUser to simulate different
authentication scenarios.
I also write unit and integration tests that make requests to secured endpoints and verify the
responses based on various user roles and permissions.
By using MockMvc in Spring MVC tests, I can assert that the security rules are correctly enforced,
checking if the access is granted or denied as expected. This ensures that the security configuration is
working properly and protecting the application as i ntended.
17) Explain salting and its usage in spring security
Salting in Spring Security means adding a random piece of data to a password before turning it into a
hash, a kind of scrambled version.
This makes every user's password hash unique, even if the actual passwords are the same. It helps
stop attackers from guessing passwords using known hash lists.
When a password needs to be checked, it's combined with its salt again, hashed, and then compared
to the stored hash to see if the password is correct. This way, the security of user passwords is
greatly increased.
18) How can you use Spring Expression Language (SpEL) for finegrained access control?
I can use Spring Expression Language (SpEL) for fine -grained access control by applying it in
annotations like @PreAuthorize in Spring Security.
With SpEL, I can create complex expressions to evaluate the user's context, such as roles,
permissions, and even specific method parameters, to decide access rights.
This allows for detailed control over who can access what in the application, making the security
checks more dynamic and tailored to the specific scenario, ensuring that users only access resources
and actions they are authorized for.
19) Explain what is AuthenticationManager  and ProviderManager in Spring security.
GenZ Career on YouTube
Subscribe for Interview Preparation
The AuthenticationManager in Spring Security is like a checkpoint that checks if user login details are
correct. The ProviderManager is a specific type of this checkpoint that uses a list of different ways
(providers) to check the login details.
It goes through each way to find one that can confirm the user’s details are valid. This setup lets
Spring Security handle different login methods, like checking against a database or an online service,
making sure the user is who they say they are.
20) When a user tries to access a resource without the necessary permissions, you want to redirect
them to a custom "access denied" page instead of displaying the default Spring Security error
message. How would you achieve this in your Spring Security configu ration?
To redirect users to a custom "access denied" page in Spring Security, I would configure the
ExceptionTranslationFilter within my security settings.
Specifically, I would set a custom access denied handler using the accessDeniedHandler method,
providing it with a URL to my custom page.
This handler intercepts the AccessDeniedException and redirects the user to the specified page,
allowing for a more user -friendly error experience. By customizing the access denied response, I can
provide clearer information or instructions to the user, im proving the overall usability of the
application.