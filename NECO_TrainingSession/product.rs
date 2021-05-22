use std::io;

fn main() {
    let mut text = String::new();
    io::stdin().read_line(&mut text).expect("error");

    let vec: Vec<&str> = text.split_whitespace().collect();

    let num1: i32 = vec[0].trim().parse().unwrap();
    let num2: i32 = vec[1].trim().parse().unwrap();

    if num1 % 2 == 0 || num2 % 2 == 0 {
        println!("Even");
    // } else if num2 % 2 == 0 {
    //     println!("Even");
    } else {
        println!("Odd");
    }
}