total_price = int(input("合計金額を教えてね(円): "))
number_pf_people = int(input("人数を教えてね(人): "))

print(number_pf_people)
print(total_price)
#print(type(total_price))<class 'str'>
#print(type(number_pf_people))<class 'str'>
print(f"一人あたり{total_price//number_pf_people}円,端数:{total_price%number_pf_people}円")


