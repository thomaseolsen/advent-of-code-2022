use std::fs::File;
use std::io::{self, BufRead};
use std::path::Path;

fn main() {
    let mut elves: Vec<i32> = Vec::new();

    if let Ok(lines) = read_lines("../input_data/01_calorie_counting.txt") {
        let mut current_elf: i32 = 0;
        for line in lines {
            if let Ok(calorie) = line {
                if calorie != "" {
                    current_elf += calorie.parse::<i32>().unwrap();
                }
                else {
                    elves.push(current_elf);
                    current_elf = 0;
                }
            }
        }
    }
    elves.sort();
    elves.reverse();
    
    println!("{}", elves[0]);
    println!("{}", top_n_sum(elves, 3));
}

fn top_n_sum(vec: Vec<i32>, n: i32) -> i32 {
    let mut ret_sum: i32 = 0;
    for i in  0..n {
        ret_sum += vec[i as usize];
    }
    return ret_sum;
}

fn read_lines<P>(filename: P) -> io::Result<io::Lines<io::BufReader<File>>>
where P: AsRef<Path>, {
    let file = File::open(filename)?;
    Ok(io::BufReader::new(file).lines())
}