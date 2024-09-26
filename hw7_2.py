# בקפיצה לגובה עם מוט פול וולט באולימפיאדה, שיא העולם הנוכחי לגברים עומד
# על 6.23 מטרים ,והוא נקבע על ידי ארמנד דופלנטיס (Duplantis Armand (בשנת 2023 .
# תוצאה של מעל 5.80 מטרים נחשבת טובה מאוד בתחרויות ברמה האולימפית, כאשר הזוכים
# לרוב קופצים מעל 6.00 מטרים.
# כתוב תוכנית בפייטון הקולטת תוצאות קפיצה לגובה של 7 מדינות באולימפיאדה .
# אם הגיעה תוצאה מתחת ל - 5.80 התעלם. רמז: continue
# אם הגיעה תוצאה טובה של 5.80 ומעלה ספור אותה
# אם אחת הקפיצות שברה את שיא העולם, קלוט את שם הספורטאי שהשיג את התוצאה
# בסוף הלולאה -
# - הדפס כמה תוצאות טובות היו, ומה הממוצע שלהם
# - הדפס מהי התוצאה הגבוהה ביותר
# - אם אחת הקפיצות שברה את שיא העולם, הדפס את שיא העולם החדש ואת שמו של
# הספורטאי. אחרת הדפס None

WORLD_RECORD: float = 6.23
new_world_record: float = None
new_world_record_name: str = None
count_good_result: int = 0
max_score: float = None
sum_good_results: float = 0
MAX_COUNT: int = 7

for jump in range(MAX_COUNT):
    result: float = float(input("what the height? "))

    if result < 5.8:
        continue
    count_good_result +=1
    sum_good_results += result

    if max_score is None or result > max_score:
        max_score = result
    if result > WORLD_RECORD:

        new_world_record = result
        print('NEW WORLD RECORD')
        new_world_record_name = input('whats the name of the jumper? ')
else:
    avg_good_score: float = None
    print(f"number of good jumps: {count_good_result}")
    if count_good_result:
        avg_good_score: float = sum_good_results / count_good_result
    print(f"good jumps avg = {avg_good_score}")
    print(f"highest score: {max_score}")
    if new_world_record:
        print(f"new world record height: {new_world_record}")
        print(f"new world record jumper name: {new_world_record_name}")
    else:
        print("no new world record achieved. None")




