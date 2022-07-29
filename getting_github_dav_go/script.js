// variables are made for the username followers and profile picture 
// to connect the html p tags so they can be edited from this java page
const username = document.querySelector("#username");
const followers = document.querySelector("#followers");
const profilePic = document.querySelector("#profilePic");

// create new function that will get the user data from the api, and convert the innerhtmnl of the desired elements
async function get_git_user(){
    //make a variable for user input to later insert into the fetch 
    const userInput = document.querySelector('input').value
    // fetch function that sets the base url as the git hub api and takes the userinput and inserts it into the end of the href to grap a specific user
    const response = await fetch("https://api.github.com/users/" + userInput);
    // converts the data retreival, that is a json object, to a variable that we can use to call for specific data
    const git_user = await response.json();

    // change the inner text, html and other elements to the specific attribute of the object desired
    username.innerText = git_user.login + ' ' + 'has';
    followers.innerText = git_user.followers + ' ' + 'followers';
    profilePic.src = git_user.avatar_url;
    
    //console log for some debugging
    console.log(userInput);
    console.log(git_user);
    //return the entire object so it can be called from and used
    return git_user;
}


