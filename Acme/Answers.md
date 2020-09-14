- What, in your opinion, is an important part of code reviews? That is, what is
  something you pay attention to when you review code, and that you appreciate
  when others do the same for your code?

  The most important thing about a code review for me is to determine if the code is readable and easy to follow. This is because in the future, I want my code to stand strong and be able to be built upon. Even if the code works, if it's impossible to read and follow than no one is going to be able to use build upon it besides myself. I may not even be able to build upon it if I forget what I was thinking in the moment of creating it. If a code review finds that the code could be written in a cleaner way, then the code has more longevity far into the future. 

 - We have an awful lot of computers here, and it gets pretty confusing with
  slightly different things running on all of them. How could containers help us
  improve this situation?

  Containers could help improve this situation by providing a common environment to run the code in. It doesn't matter what the operating system or programs that any computer is using, the container makes sure that the correct environment is created to be able to run the file smoothly. This also makes sure that the dependancies and versions of programs are correct. For example, if pandas takes out the sample capability in their newest update, but your code depends on it, it doesn't matter what version of pandas another user has, a container will import the required version of pandas  