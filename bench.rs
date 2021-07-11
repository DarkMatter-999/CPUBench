
fn main() {
    for i in 2..100000 {
        let mut prime = true;
        for j in 2..i {
            if i % j == 0 {
                prime = false;
                break;
            }
        }
        if prime {
            println!("{}", i);
        }
    }
}
