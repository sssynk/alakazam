from alakazam.core.checker import test_proxy_file

print()
print("🪄 alakazam proxy checker")
print()

in_file = input("✨ Enter the path to the file with proxies: ")
out_file = input("✨ Enter the path to the output file (valid proxies): ")
threads = int(input("✨ Enter the number of threads (default 25, can go up to >500): ") or 25)

# check if the file exists
try:
    with open(in_file, "r") as f:
        pass
except FileNotFoundError:
    print(f"❌ File {in_file} not found")
    exit(1)

print("Starting to check proxies...")

count_working, count_total, out_file = test_proxy_file(in_file, out_file, threads=threads)

print(f"🪄 Checked {count_total} proxies, {count_working} are working. Results saved in {out_file}")
