import pyfiglet
from rich.console import Console
from rich.progress import track
from rich.table import Table
from InquirerPy import inquirer
from InquirerPy.base.control import Choice
from InquirerPy.separator import Separator
from job_api import find_job
from open_ai_api import improve_skills
from about_us import about_us
from speaktoai import SpeakToAI

console = Console()

def main():
    console.print(pyfiglet.figlet_format("Positionday", font="slant"), style="bold red")

    # Ask the user to choose an option
    option = inquirer.select(
        message="Choose an option:",
        choices=[
            Choice("Find a job", name="Find a job"),
            Choice("Improve your skills", name="Improve your skills"),
            Choice("Speak to Sam (Career coach)", name="Speak to Sam (Career coach)"),
            Choice("About Positionday", name="About Positionday"),
            Choice("Help", name="Help"),
        ],
        default="Find a job",
        qmark="?",
        pointer=">",
    ).execute()

    # Call the corresponding function based on the user's choice
    if option == "Find a job":
        # Ask the user for the job search query, country, and location
        query = inquirer.text(message="Enter your job search query:").execute()
        country = inquirer.text(message="Enter the country:").execute()
        location = inquirer.text(message="Enter the location:").execute()

        # Call the find_job function and display the results with text animation and a progress bar
        console.print("Searching for jobs...", style="bold yellow")
        filename = find_job(query, country, location)
        console.print(f"CSV saved as {filename}", style="bold green")

    elif option == "Improve your skills":
        # Ask the user for the job role
        role = inquirer.text(message="Enter your job role:").execute()

        # Call the improve_skills function and display the results with text animation
        console.print("Retrieving information about improving skills...", style="bold yellow")
        skills = improve_skills(role)
        console.print("Here are some skills you can improve:", style="bold green")
        for skill in skills:
            console.print(f"- {skill}", style="bold blue")

    elif option == "Speak to Sam (Career coach)":
        # Initialize SpeakToAI and start the conversation loop
        speak_to_ai = SpeakToAI()
        speak_to_ai.run()

    elif option == "About Positionday":
        # Call the about_us function and display the results with text animation
        console.print("Retrieving information about Positionday...", style="bold yellow")
        about = about_us()
        console.print("Here's some information about Positionday:", style="bold green")
        console.print(f"- Name: {about['name']}", style="bold blue")
        console.print(f"- Description: {about['description']}", style="bold blue")
        console.print(f"- Website: {about['website']}", style="bold blue")

    elif option == "Help":
        # Display a list of all the available options and their descriptions
        console.print("Here are the available options:", style="bold green")
        console.print("- Find a job: Search for jobs based on a query", style="bold blue")
        console.print("- Improve your skills: Retrieve information about improving skills based on a job role", style="bold blue")
        console.print("- Speak to Sam (Career coach): Have a conversation with Sam, the career coach", style="bold blue")
        console.print("- About Positionday: Display information about Positionday", style="bold blue")
        console.print("- Help: Display a list of all the available options and their descriptions", style="bold blue")

if __name__ == '__main__':
    main()
