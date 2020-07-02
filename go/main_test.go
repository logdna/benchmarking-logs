package main

import (
	"testing"
)

func BenchmarkBenchyStr(b *testing.B) {
	for i := 0; i < b.N; i++ {
		BenchyStr()
	}
}