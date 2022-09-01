from PIL import Image, ImageTk


class CreateImage:
    @staticmethod
    def create_weather_symbols():
        weather_symbols = []
        image_x, image_y = 25, 385
        for i in range(0, 4):
            pic = Image.open(f"icon/types/{i}.png")
            picture = pic.resize((30, 30))
            current_picture = ImageTk.PhotoImage(picture)
            weather_symbols.append(current_picture)
            image_x += 50

            return weather_symbols[i], image_x, image_y
