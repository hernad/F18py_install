import f18ziherpy

def main():
    callback = lambda x,y: x+y+3
    f18ziherpy.vminit()
    f18ziherpy.run('MAIN0',1,0)
    f18ziherpy.run('MAIN',0,1)

if __name__ == "__main__":
    main()