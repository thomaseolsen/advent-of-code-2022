package main

import (
    "bufio"
    "fmt"
    "log"
    "os"
    "sort"
    "strconv"
)


// readLines reads a whole file into memory
// and returns a slice of its lines.
func readLines(path string) ([]string, error) {
    file, err := os.Open(path)
    if err != nil {
        return nil, err
    }
    defer file.Close()

    var lines []string
    scanner := bufio.NewScanner(file)
    for scanner.Scan() {
        lines = append(lines, scanner.Text())
    }
    return lines, scanner.Err()
}

func topNSum(lst []int, n int) (int) {
    retSum := 0
    for i := 0; i < n; i++ {
        retSum += lst[i]
    }
    return retSum
}

func main() {
    lines, err := readLines("../input_data/01_calorie_counting.txt")
    if err != nil {
        log.Fatalf("readLines: %s", err)
    }

    elves := []int{}
    current_elf := 0
    for _, s := range lines {
        if s != "" {
            int_s, err := strconv.Atoi(s)
            if err == nil {
                current_elf += int_s
            }
        } else {
            elves = append(elves, current_elf)
            current_elf = 0
        }
    }
    sort.Sort(sort.Reverse(sort.IntSlice(elves)))
    fmt.Println(elves[0])  // 71,300
    fmt.Println(topNSum(elves, 3))  // 209,691
}