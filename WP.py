import pywhatkit as kit
import datetime

# Функция для отправки сообщения в WhatsApp
def send_whatsapp_message(phone_number, message, hour, minute):
    try:
        kit.sendwhatmsg(phone_number, message, hour, minute)
        print(f"Сообщение отправлено на {phone_number} в {hour}:{minute}.")
    except Exception as e:
        print(f"Произошла ошибка: {e}")

# Ввод данных от пользователя
if __name__ == "__main__":
    phone_number = input("Введите номер телефона получателя с кодом страны (например, +1234567890): ")
    message = input("Напишите ваше сообщение: ")
    
    # Установка времени отправки
    print("Выберите время отправки (в 24-часовом формате):")
    hour = int(input("Часы (0-23): "))
    minute = int(input("Минуты (0-59): "))
    
    # Проверка правильности введенного времени
    now = datetime.datetime.now()
    if (hour < 0 or hour > 23) or (minute < 0 or minute > 59):
        print("Пожалуйста, введите корректное время.")
    else:
        send_whatsapp_message(phone_number, message, hour, minute)

