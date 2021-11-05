from appserver import app, load_model

weights_loaded="./checkpoint/yolov4"
labels_path = "./checkpoint/yolov4/labelmap.txt"

if __name__ == '__main__':

    load_model(weights_loaded)

    print("Loaded tensor model.......")

    app.debug = True
    app.run(host = "0.0.0.0")