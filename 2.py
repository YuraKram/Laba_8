import cv2, time


count = int(input('Сколько всего меток надо распознать?' + '\n'))
def video_processing():
    cap = cv2.VideoCapture(0)
    down_points = (640, 480)
    i = 0
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        frame = cv2.resize(frame, down_points, interpolation=cv2.INTER_LINEAR)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        gray = cv2.GaussianBlur(gray, (21, 21), 0)
        ret, thresh = cv2.threshold(gray, 110, 255, cv2.THRESH_BINARY_INV)

        contours, hierarchy = cv2.findContours(thresh,
                            cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
        if len(contours) > 0:
            sort_contours = sorted(contours, key = cv2.contourArea)[::-1]
            if len(contours) < count:
                continue
            for marks in range(count):
                x, y, w, h = cv2.boundingRect(sort_contours[marks])
                rec = cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
                if down_points[0]/2 - 200 < x < down_points[0]/2 + 200 and down_points[1]/2 - 200 < y < down_points[1]/2 + 200:
                    cv2.putText(rec, 'falls into the area', (x, y - 10),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        0.5, (36, 255, 12), 1)
                else:
                    cv2.putText(rec, 'falls not into the area', (x, y - 10),
                                cv2.FONT_HERSHEY_SIMPLEX,
                                0.5, (36, 255, 12), 1)
                if i % 5 == 0:
                    a = x + (w // 2)
                    b = y + (h // 2)
                    print(a, b)

        cv2.imshow('frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

        time.sleep(0.1)
        i += 1

    cap.release()


if __name__ == '__main__':
    #image_processing()
    video_processing()

cv2.waitKey(0)
cv2.destroyAllWindows()