using System;
using System.Collections.Generic;
using System.Linq;

namespace AdventOfCode2017
{
  class Day6
  {
    public static void Main(string[] args)
    {
      Util.CheckAnswer(new[] { 0, 2, 7, 0 }, NumRedistributionCycles, 5);
      Util.CheckAnswer(new[] { 0, 2, 7, 0 }, NumRedistributionCyclesToSeeTwice, 4);

      string text = Util.GetFileContents("Day6");
      int[] inputBuffers = text.Split(new[] { '\t', ' ' }, StringSplitOptions.RemoveEmptyEntries).Select(str => int.Parse(str)).ToArray();

      Part1(inputBuffers);
      Part2(inputBuffers);

      Console.ReadKey();
    }

    private static void Part1(int[] inputBuffers)
    {
      Console.WriteLine(NumRedistributionCycles(inputBuffers));
    }

    private static void Part2(int[] inputBuffers) { 
      Console.WriteLine(NumRedistributionCyclesToSeeTwice(inputBuffers));
    }

    private static int NumRedistributionCycles(int[] initialBlocks)
    {
      State current = new State(initialBlocks);
      ISet<State> seen = new HashSet<State>();
      seen.Add(current);

      int cycles = 0;
      while (true)
      {
        cycles++;

        State next = current.Next();

        if (seen.Contains(next))
        {
          break;
        }

        seen.Add(next);
        current = next;
      }

      return cycles;
    }

    private static int NumRedistributionCyclesToSeeTwice(int[] initialBlocks)
    {
      State current = new State(initialBlocks);
      ISet<State> seen = new HashSet<State>();
      seen.Add(current);

      int cycles = 0;
      State toSeeAgain = null;

      while (true)
      {
        cycles++;

        State next = current.Next();

        if (seen.Contains(next))
        {
          toSeeAgain = next;
          break;
        }

        seen.Add(next);
        current = next;
      }

      cycles = 0;
      current = toSeeAgain;
      while (true)
      {
        cycles++;

        State next = current.Next();
        if (next.Equals(toSeeAgain))
        {
          break;
        }

        current = next;
      }

      return cycles;
    }

    private class State
    {
      public readonly int[] blocks;
      private int? hashCode;

      public State(int[] blocks)
      {
        this.blocks = blocks;
      }

      public State Next()
      {
        int[] newBlocks = new int[this.blocks.Length];
        Array.Copy(this.blocks, newBlocks, this.blocks.Length);

        int redistributedBank = this.GetIndexOfMemoryBankWithMostBlocks();
        int numBlocks = this.blocks[redistributedBank];
        newBlocks[redistributedBank] = 0;

        int blocksForEachBank = numBlocks / this.blocks.Length;

        for (int blockNum = 0; blockNum < newBlocks.Length; blockNum++)
        {
          newBlocks[blockNum] += blocksForEachBank;
        }

        int leftoverBlocks = numBlocks % this.blocks.Length;

        int i = 0;
        while (i < leftoverBlocks)
        {
          int bufferToAddTo = redistributedBank + i + 1;
          if (bufferToAddTo >= newBlocks.Length)
          {
            bufferToAddTo -= newBlocks.Length;
          }

          newBlocks[bufferToAddTo]++;

          i++;
        }

        return new State(newBlocks);
      }

      public int GetIndexOfMemoryBankWithMostBlocks()
      {
        return Array.IndexOf(this.blocks, this.blocks.Max());
      }

      public override bool Equals(object obj)
      {
        State other = obj as State;

        if (other == null)
        {
          return false;
        }

        return this.blocks.Zip(other.blocks, (a, b) => a == b).All(equality => equality == true);
      }

      public override int GetHashCode()
      {
        if (this.hashCode.HasValue)
        {
          return this.hashCode.Value;
        }

        this.hashCode = 0;

        for (int i = 0; i < this.blocks.Length; i++)
        {
          this.hashCode += (int)Math.Pow(this.blocks[i], i + 1);
        }

        return this.hashCode.Value;
      }

      public override string ToString()
      {
        return string.Join(" ", this.blocks);
      }
    }
  }
}
