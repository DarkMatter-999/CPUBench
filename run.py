import os
import timeit

colors = str(input("Do you want colored output in colsole? \n!(pip install colorama)\n[Y/N] "))

if colors == "Y":

    colors = True
else:
    colors = False

def onerr(e):
    print(Fore.RED + " !!!!! Could not build !!!!" + Fore.RESET)
    print(e)

def build():
    target = str(input(Fore.WHITE + "What benchmark do you want to build:\n" +
    Fore.GREEN + "1." +Fore.RESET+ " GCC C\n" +
    Fore.GREEN + "2." +Fore.RESET+ " GCC C++\n" +
    Fore.GREEN + "3." +Fore.RESET+ " LLVM Rust\n" +
    Fore.GREEN + "4." +Fore.RESET+ " All\n"
    ))
    if target == "1":
        try:
            print(Fore.GREEN + "Building C with GCC" + Fore.RESET)
            if os.name == "nt":
                os.system("gcc.exe bench.c -o gcc_c.exe")
            elif os.name == "posix":
                os.system("gcc bench.c -o gcc_c")
            else:
                onerr("ERROR: Support for " + os.name + " not implemented")
                raise
        except Exception as e:
            onerr(e)

    elif target == "2":
        try:
            print(Fore.GREEN + "Building C++ with GCC" + Fore.RESET)
            if os.name == "nt":
                os.system("g++.exe bench.cpp -o gcc_cpp.exe")
            elif os.name == "posix":
                os.system("g++ bench.cpp -o gcc_cpp")
            else:
                onerr("ERROR: Support for " + os.name + " not implemented")
                raise
        except Exception as e:
            onerr(e)

    elif target == "3":
        try:
            print(Fore.GREEN + "Building Rust with RustC(LLVM)" + Fore.RESET)
            if os.name == "nt":
                os.system("rustc.exe bench.rs -o llvm_rust.exe")
            elif os.name == "posix":
                os.system("rustc bench.rs -o llvm_rust")
            else:
                onerr("ERROR: Support for " + os.name + " not implemented")
                raise
        except Exception as e:
            onerr(e)

    elif target == "4":
        try:
            print(Fore.GREEN + "Building all" + Fore.RESET)
            print(Fore.GREEN + "Building C with GCC" + Fore.RESET)
            if os.name == "nt":
                os.system("gcc.exe bench.c -o gcc_c.exe")
            elif os.name == "posix":
                os.system("gcc bench.c -o gcc_c")
            else:
                onerr("ERROR: Support for " + os.name + " not implemented")
                raise

            print(Fore.GREEN + "Building C++ with GCC" + Fore.RESET)
            if os.name == "nt":
                os.system("g++.exe bench.cpp -o gcc_cpp.exe")
            elif os.name == "posix":
                os.system("g++ bench.cpp -o gcc_cpp")
            else:
                onerr("ERROR: Support for " + os.name + " not implemented")
                raise

            print(Fore.GREEN + "Building Rust with RustC(LLVM)" + Fore.RESET)
            if os.name == "nt":
                os.system("rustc.exe bench.rs -o llvm_rust.exe")
            elif os.name == "posix":
                os.system("rustc bench.rs -o llvm_rust")
            else:
                onerr("ERROR: Support for " + os.name + " not implemented")
                raise

        except Exception as e:
            onerr(e)

def time():
    imports = "import os"

    target = str(input(Fore.WHITE + "What benchmark do you want to run:\n" +
    Fore.GREEN + "1." +Fore.RESET+ " GCC C\n" +
    Fore.GREEN + "2." +Fore.RESET+ " GCC C++\n" +
    Fore.GREEN + "3." +Fore.RESET+ " LLVM Rust\n" +
    Fore.GREEN + "4." +Fore.RESET+ " All\n"
    ))
    if target == "1":
        if os.name == "nt":
            command = """
os.system('gcc_c.exe')
            """
        elif os.name == "posix":
            command = """
os.system('gcc_c')
            """
        else:
            onerr("ERROR: Support for " + os.name + " not implemented")
            raise

        print(f"Execution time is: {timeit.timeit(setup = imports, stmt = command, number = 3)/3}")

    elif target == "2":

        if os.name == "nt":
            command = """
os.system('gcc_cpp.exe')
            """
        elif os.name == "posix":
            command = """
os.system('gcc_cpp')
            """
        else:
            onerr("ERROR: Support for " + os.name + " not implemented")
            raise

        print(f"Execution time is: {timeit.timeit(setup = imports, stmt = command, number = 3)/3}")

    elif target == "3":

        if os.name == "nt":
            command = """
os.system('llvm_rust.exe')
            """
        elif os.name == "posix":
            command = """
os.system('llvm_rust.exe')
            """
        else:
            onerr("ERROR: Support for " + os.name + " not implemented")
            raise

        print(f"Execution time is: {timeit.timeit(setup = imports, stmt = command, number = 3)/3}")

    elif target == "4":
        if os.name == "nt":
            command1 = """
os.system('gcc_c.exe')
            """
            command2 = """
os.system('gcc_cpp.exe')
            """
            command3 = """
os.system('llvm_rust.exe')
            """
        elif os.name == "posix":
            command1 = """
os.system('gcc_c')
            """
            command2 = """
os.system('gcc_cpp')
            """
            command3 = """
os.system('llvm_rust')
            """
        else:
            onerr("ERROR: Support for " + os.name + " not implemented")
            raise

        C = timeit.timeit(setup = imports, stmt = command1, number = 3)/3
        CPP =  timeit.timeit(setup = imports, stmt = command2, number = 3)/3
        RUST =  timeit.timeit(setup = imports, stmt = command3, number = 3)/3

        print(f"Execution time for C is:{C}")
        print(f"Execution time for C++ is:{CPP}")
        print(f"Execution time for Rust is:{RUST}")


if __name__ == '__main__':
    if colors:
        from colorama import Fore
    else:
        class Fore:
            GREEN = ""
            RED = ""
            WHITE = ""
            RESET = ""

    build()
    time()
