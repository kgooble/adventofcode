using System;
using System.Collections.Generic;
using System.Linq;

namespace AdventOfCode2017
{
  class Day3
  {
    public static void Main(string[] args)
    {
      Util.CheckAnswer(1, Part1SpiralDistance, 0);
      Util.CheckAnswer(12, Part1SpiralDistance, 3);
      Util.CheckAnswer(23, Part1SpiralDistance, 2);
      Util.CheckAnswer(1024, Part1SpiralDistance, 31);

      Console.WriteLine(Part1SpiralDistance(325489));

      Console.WriteLine(Part2ValueInSpiralGreaterThan(325489));

      Console.ReadKey();
    } 

    private static int Part1SpiralDistance(int position)
    {
      if (position == 1)
      {
        return 0;
      }

      int firstCorner = FindNearestOddSquareGreaterThan(position);
      int width = (int)Math.Sqrt(firstCorner);
      int distBetweenCorners = width - 1;

      int secondCorner = firstCorner - distBetweenCorners;
      int thirdCorner = secondCorner - distBetweenCorners;
      int fourthCorner = thirdCorner - distBetweenCorners;
      int innerCorner = fourthCorner - distBetweenCorners + 1;

      int midPoint = 0;

      if (firstCorner >= position && position >= secondCorner)
      {
        midPoint = (firstCorner + secondCorner) / 2;
      }
      else if (secondCorner > position && position >= thirdCorner)
      {
        midPoint = (secondCorner + thirdCorner) / 2;
      }
      else if (thirdCorner > position && position >= fourthCorner)
      {
        midPoint = (thirdCorner + fourthCorner) / 2;
      }
      else if (fourthCorner > position && position >= innerCorner)
      {
        midPoint = (fourthCorner + innerCorner) / 2;
      }

      return Math.Abs(midPoint - position) + (width / 2);
    }

    private static int Part2ValueInSpiralGreaterThan(int upTo)
    {
      return GenerateSpiral(upTo);
    }

    private static int GenerateSpiral(int untilValue, int maxSearchDepth = 1000)
    {
      var spiral = new Dictionary<Pos, int>();
      Dir dir = Dir.Down;
      Pos current = new Pos(0, 0);
      spiral[current] = 1;

      int i = 0;
      while (true)
      {
        Movement nextMovement = NextMovement(spiral, current, dir);
        int val = SumOfAdjacentNeighbours(spiral, nextMovement.pos);
        current = nextMovement.pos;
        dir = nextMovement.dir;
        spiral[current] = val;

        if (val > untilValue)
        {
          return val;
        }

        if (++i > maxSearchDepth)
        {
          throw new Exception($"Couldn't find value greater than {untilValue} after trying {maxSearchDepth} iterations.");
        }
      }
    }

    private static int FindNearestOddSquareGreaterThan(int number)
    {
      int sqrt = (int)Math.Ceiling(Math.Sqrt(number));

      if (sqrt % 2 == 1)
      {
        return (int)Math.Pow(sqrt, 2);
      } else
      {
        return (int)Math.Pow(sqrt + 1, 2);
      }
    }

    private struct Pos
    {
      public readonly int x;
      public readonly int y;

      public Pos(int x, int y)
      {
        this.x = x;
        this.y = y;
      }

      public Pos Next(Dir dir)
      {
        switch (dir)
        {
          case Dir.Left:
            return new Pos(this.x - 1, this.y);
          case Dir.Down:
            return new Pos(this.x, this.y + 1);
          case Dir.Right:
            return new Pos(this.x + 1, this.y);
          case Dir.Up:
            return new Pos(this.x, this.y - 1);
        }

        throw new ArgumentException("Unexpected dir: " + dir);
      }

      public IEnumerable<Pos> GetNeighbours()
      {
        var neighbours = new List<Pos>();

        neighbours.Add(this.Next(Dir.Up));
        neighbours.Add(this.Next(Dir.Left));
        neighbours.Add(this.Next(Dir.Right));
        neighbours.Add(this.Next(Dir.Down));

        neighbours.Add(this.Next(Dir.Up).Next(Dir.Left));
        neighbours.Add(this.Next(Dir.Up).Next(Dir.Right));
        neighbours.Add(this.Next(Dir.Down).Next(Dir.Left));
        neighbours.Add(this.Next(Dir.Down).Next(Dir.Right));

        return neighbours;
      }

      public override string ToString()
      {
        return $"({this.x}, {this.y})";
      }
    }

    private enum Dir
    {
      Left,
      Right,
      Up,
      Down
    }

    private struct Movement
    {
      public readonly Pos pos;
      public readonly Dir dir;

      public Movement(Pos pos, Dir dir)
      {
        this.pos = pos;
        this.dir = dir;
      }
    }

    private static Dir NextDirCW(Dir dir)
    {
      switch (dir)
      {
        case Dir.Left:
          return Dir.Down;
        case Dir.Down:
          return Dir.Right;
        case Dir.Right:
          return Dir.Up;
        case Dir.Up:
          return Dir.Left;
      }

      throw new ArgumentException("Unexpected dir: " + dir);
    }

    private static Movement NextMovement(Dictionary<Pos, int> filled, Pos currentPosition, Dir lastDirection)
    {
      Dir potentialNextDir = NextDirCW(lastDirection);
      Pos potentialNextPos = currentPosition.Next(potentialNextDir);

      if (filled.ContainsKey(potentialNextPos))
      {
        return new Movement(currentPosition.Next(lastDirection), lastDirection);
      }

      return new Movement(potentialNextPos, potentialNextDir);
    }

    private static int SumOfAdjacentNeighbours(Dictionary<Pos, int> spiral, Pos current)
    {
      int sum = 0;
      foreach (Pos neighbour in current.GetNeighbours())
      {
        if (spiral.ContainsKey(neighbour))
        {
          sum += spiral[neighbour];
        }
      }
      return sum;
    }
  }
}
