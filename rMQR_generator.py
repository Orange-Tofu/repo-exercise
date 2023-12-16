from rmqrcode import rMQR, QRImage
import rmqrcode


def Generator(data, location):
    qr = rMQR.fit(
        data,
        ecc=rmqrcode.ErrorCorrectionLevel.M,
        fit_strategy=rmqrcode.FitStrategy.MINIMIZE_HEIGHT
    )

    image = QRImage(qr, module_size=8)
    # image.show()

    #Change image location appropraitely
    # location = "M:\\CS\\TitTat\\TechnoSeek-V2.0"
    image.save(location + "\\clue.png")
    print(f"Data:{data}, Image saved at location:{location}")

# Generator("Hello World")