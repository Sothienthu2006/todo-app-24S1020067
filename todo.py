tasks = []

def main():
    while True:
        print("\n=== MENU ===")
        print("1. Xem danh sách công việc")
        print("2. Thêm công việc")
        print("3. Thoát")

        choice = input("Chọn chức năng: ")

        if choice == "1":
            print("Danh sách công việc:", tasks)

        elif choice == "2":
            new_task = input("Nhập công việc mới: ")
            tasks.append(new_task)
            print("Đã thêm!")

        elif choice == "3":
            print("Thoát...")
            break

        else:
            print("Lựa chọn không hợp lệ.")

if __name__ == "__main__":
    main()
