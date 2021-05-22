use std::io;

fn main() {
    let mut text = String::new();
    io::stdin().read_line(&mut text).expect("error");

    let vec: Vec<&str> = text.split_whitespace().collect();

    let a: i32 = vec[0].trim().parse().unwrap();
    let b: i32 = vec[1].trim().parse().unwrap();
    let x: i32 = vec[2].trim().parse().unwrap();

    if a <= x  && x <= a+b {
        println!("YES");
    
    } else {
        println!("NO");
    }
}