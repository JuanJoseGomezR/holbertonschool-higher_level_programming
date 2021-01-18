﻿using System;

namespace vectori
{
    /// <summary>Contains operations to perform on vectors.</summary>
    class VectorMath
    {
        /// <summary>Adds two vectors</summary>
        public static double[] Add(double[] vector1, double[] vector2) {
            double[] fail = { -1, -1 };
            if (vector1 is null || vector1.Rank != 1 || vector1.Length < 2 || vector1.Length > 3)
                return fail;
            if (vector2 is null || vector2.Rank != 1 || vector2.Length < 2 || vector2.Length > 3)
                return fail;
            if (vector1.Length != vector2.Length)
                return fail;

            double[] ret = new double[vector1.Length];
            for (int i = 0; i < ret.Length; i++)
                ret[i] = vector1[i] + vector2[i];
            return ret;
        }
    }
}