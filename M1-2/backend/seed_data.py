import csv
import os

from firebase.client import db


CSV_PATH = os.path.join(
    os.path.dirname(__file__),
    "..",
    "data",
    "nvda.csv",
)


def clean_price(value: str) -> float:
    return float(value.replace("$", "").replace(",", ""))


def clean_volume(value: str) -> int:
    return int(value.replace(",", ""))


def seed_data():
    data_ref = db.collection("data")

    batch = db.batch()
    count = 0

    with open(CSV_PATH, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            date = row["Date"]
            close = clean_price(row["Close/Last"])
            volume = clean_volume(row["Volume"])
            open_price = clean_price(row["Open"])
            high = clean_price(row["High"])
            low = clean_price(row["Low"])

            doc_ref = data_ref.document()

            batch.set(doc_ref, {
                "date": date,
                "value": close,
                "volume": volume,
                "open": open_price,
                "high": high,
                "low": low,
                "memo": "NVDA",
            })

            count += 1

            # Firestore batch 최대 500개 단위
            if count % 500 == 0:
                batch.commit()
                print(f"{count}개 데이터 저장 완료")
                batch = db.batch()

    # 남은 데이터 저장
    if count % 500 != 0:
        batch.commit()

    print(f"총 {count}개 데이터 저장 완료")


if __name__ == "__main__":
    seed_data()