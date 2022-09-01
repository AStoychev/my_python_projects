class WeatherComponents:
    @staticmethod
    def town_location(location):
        current_location = location.split(" ")

        if current_location[2] != " ":
            loc = current_location[1] + " " + current_location[2]
        else:
            loc = current_location[1]
        return loc

    @staticmethod
    def town_temperature(temperature):
        temperature = temperature.strip()
        return temperature

    @staticmethod
    def town_prediction(weather_prediction):
        weather_prediction = weather_prediction.strip()
        data = weather_prediction.split("\n")
        time = data[0]
        time_prediction = data[-1]

        words = time_prediction.split()
        if len(words) > 3:
            weather_info = words[0:3]
            weather_info_1 = words[4:]
            predictions = " ".join(weather_info)
            predictions_1 = " ".join(weather_info_1)
            predictions = predictions.rstrip(",")
            predictions_1 = predictions_1.rstrip(",")
            final_prediction = f"{predictions}\n{predictions_1}"
        else:
            final_prediction = time_prediction
        return time, final_prediction
