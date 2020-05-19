from kvadratas import Kvadratas

print(dir(Kvadratas))

def results():
    kvadr = Kvadratas(2.0)
    print("Krastine: 2, istrizaine:", kvadr.diagonal())
    
    kvadr = Kvadratas(5.0)
    print("Krastine: 5, istrizaine:", kvadr.diagonal())
    
    
    kvadr = Kvadratas(1.5)
    print("Krastine: 1.5, istrizaine:", kvadr.diagonal())


results()
