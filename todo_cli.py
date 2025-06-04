import os

TASKS_FILE = 'todo.txt'

def load_tasks(filename):
    if not os.path.exists(filename):
        return []
    with open(filename, 'r', encoding='utf-8') as f:
        return [line.strip() for line in f if line.strip()]

def save_tasks(filename, tasks):
    with open(filename, 'w', encoding='utf-8') as f:
        for task in tasks:
            f.write(task + '\n')

def main():
    tasks = load_tasks(TASKS_FILE)
    while True:
        print("\nTodo List:")
        for i, t in enumerate(tasks, 1):
            print(f"{i}. {t}")
        print("\nCommands: [a]dd, [r]emove, [q]uit")
        cmd = input("Choose an option: ").strip().lower()
        if cmd == 'a':
            task = input("Enter new task: ").strip()
            if task:
                tasks.append(task)
        elif cmd == 'r':
            num = input("Enter task number to remove: ").strip()
            if num.isdigit():
                idx = int(num) - 1
                if 0 <= idx < len(tasks):
                    tasks.pop(idx)
        elif cmd == 'q':
            break
        else:
            print("Unknown command.")
    save_tasks(TASKS_FILE, tasks)
    print(f"Tasks saved to {TASKS_FILE}")

if __name__ == '__main__':
    main()
