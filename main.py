def search_colors(weather, mood, event):
    with open('colourdata.txt', 'r') as file:
        lines = file.readlines()

    matching_colors = []
    for line in lines:
        color, weather_data, mood_data, event_data = map(str.strip, line.split(','))

        if (
            weather.lower() == weather_data.lower()
            and mood.lower() == mood_data.lower()
            and (event.lower() == 'none' or event.lower() == event_data.lower())
        ):
            matching_colors.append(color)

    return matching_colors

def main():
    print("Welcome to the Nail Colour Picker!")

    # Predefined lists for weather, mood, and events
    weather_options = ['Sunny', 'Rainy', 'Cloudy', 'Snowy', 'Clear']
    mood_options = ['Happy', 'Sad', 'Excited', 'Calm', 
                    'Energetic', 'Peaceful', 'Adventurous']
    event_options = ['None', 'Birthday', 'Wedding', 'Concert',
                     'Vacation', 'Music Festival', 'Party', 'Christmas', 'Anniversary',
                     'Shopping Day', 'Formal Dinner', 'Date Night']

    # Prompt user to pick from the lists
    weather = get_user_choice("Pick the weather: ", weather_options)
    mood = get_user_choice("Pick your mood: ", mood_options)
    event = get_user_choice("Pick the event): ", event_options)

    matching_colors = search_colors(weather, mood, event)

    if matching_colors:
        print("We've found the perfect colour(s) for you!")
        print(f"{', '.join(matching_colors)}")
    else:
        print("Hmm, maybe go with a classic French tip?.")


def get_user_choice(prompt, options):
    while True:
        print(prompt)
        for i, option in enumerate(options, 1):
            print(f"{i}. {option}")
        
        user_input = input("Enter the number of your choice: ")
        try:
            choice_index = int(user_input) - 1
            if 0 <= choice_index < len(options):
                return options[choice_index]
            else:
                print("Invalid choice. Please enter a valid number.")
        except ValueError:
            print("Invalid input. Please enter a number.")


if __name__ == "__main__":
    main()