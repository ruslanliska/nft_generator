from handlers.storage import banner
from handlers.slime_modification import create_image
from pyfade import Fade, Colors


def main():
    print(Fade.Vertical(Colors.red_to_blue, banner))
    print("\nHow much NFT's do you want to generate?")
    amount = int(input("-> "))
    for number in range(amount):
        slime_num = number + 1
        create_image(slime_num)
        print(f"[slime-{slime_num}][{amount}/{slime_num}] - succesfully created")


if __name__ == "__main__":
    main()
