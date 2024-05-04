price_rubles = int(input("Стоимость пирожка (рубли): "))
price_kopeks = int(input("Стоимость пирожка (копейки): "))
quantity = int(input("Сколько пирожков: "))

total_kopeks = price_rubles * 100 + price_kopeks
total_payment_kopeks = total_kopeks * quantity

total_rubles = total_payment_kopeks // 100
remaining_kopeks = total_payment_kopeks % 100

print(f"К оплате: {total_rubles} руб. {remaining_kopeks} коп.")