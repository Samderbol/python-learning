import pysnooper

@pysnooper.snoop()
def demo_func():
    profile = {}
    profile["name"] = "pysnooper learning"
    profile["age"] = 21
    profile["gender"] = "male"
    return profile

def main():
    profile = demo_func()

main()