#!/usr/bin/env python3
"""
Analyze mutualism simulation data under the shuffle condition
and compare it with the noshuffle baseline.
K=0.5, b=0.4, c0 < c1 (upper-triangular 210-cell grid).
"""

import csv
import os
import sys
from collections import defaultdict
import math

BASE = os.path.expanduser("~/results")
K = 0.5
B = 0.4

def load_con(path):
    if not os.path.exists(path):
        return None
    with open(path) as f:
        return list(csv.DictReader(f))

def coop(row):
    return float(row["qBSeen"])

def sorted_rows(rows):
    return sorted(rows, key=lambda r: (float(r["c0"]), float(r["c1"])))

def mut_path(shuffle, gs, mech, dilemma, fset):
    cond = f"{shuffle}_cost0.001_{gs}"
    return os.path.join(BASE, "mutualism", cond, mech, str(dilemma), "pop_2",
                        f"csv_{fset}_for_image.con")

def main():
    mechs = ["_", "M", "P", "MP", "MPQ", "IMP", "IJMPQ"]
    dilemmas = [1, 2]
    groupsizes = ["128", "4"]
    
    print("=" * 80)
    print("MUTUALISM SHUFFLE VS NOSHUFFLE ANALYSIS")
    print("=" * 80)
    
    # 1. Overall Cooperation comparison (Mean across all 210 cells)
    print("\n--- 1. OVERALL COOPERATION (Mean qBSeen across all 210 cells) ---")
    print(f"{'Mechanism':10s} | {'Dilemma':8s} | {'GS':4s} | noshuffle (fset_0 / fset_1) | shuffle (fset_0 / fset_1)")
    print("-" * 85)
    
    for mech in mechs:
        for dilemma in dilemmas:
            d_name = "PD (d1)" if dilemma == 1 else "SD (d2)"
            for gs in groupsizes:
                # Load noshuffle
                path_no_0 = mut_path("noshuffle", gs, mech, dilemma, 0)
                path_no_1 = mut_path("noshuffle", gs, mech, dilemma, 1)
                rows_no_0 = load_con(path_no_0)
                rows_no_1 = load_con(path_no_1)
                
                # Load shuffle
                path_sh_0 = mut_path("shuffle", gs, mech, dilemma, 0)
                path_sh_1 = mut_path("shuffle", gs, mech, dilemma, 1)
                rows_sh_0 = load_con(path_sh_0)
                rows_sh_1 = load_con(path_sh_1)
                
                if not (rows_no_0 and rows_sh_0):
                    continue
                
                avg_no_0 = sum(coop(r) for r in rows_no_0) / len(rows_no_0)
                avg_no_1 = sum(coop(r) for r in rows_no_1) / len(rows_no_1)
                avg_sh_0 = sum(coop(r) for r in rows_sh_0) / len(rows_sh_0)
                avg_sh_1 = sum(coop(r) for r in rows_sh_1) / len(rows_sh_1)
                
                print(f"{mech:10s} | {d_name:8s} | {gs:4s} | {avg_no_0:.3f} / {avg_no_1:.3f}          | {avg_sh_0:.3f} / {avg_sh_1:.3f}")
        print("-" * 85)

    # 2. Role Split Asymmetry (fset_0 > fset_1 fraction)
    print("\n--- 2. ROLE SPLIT: Fraction of cells where fset_0 > fset_1 ---")
    print(f"{'Mechanism':10s} | {'Dilemma':8s} | {'GS':4s} | noshuffle | shuffle")
    print("-" * 55)
    
    for mech in mechs:
        for dilemma in dilemmas:
            d_name = "PD (d1)" if dilemma == 1 else "SD (d2)"
            for gs in groupsizes:
                # Noshuffle
                p_no_0 = mut_path("noshuffle", gs, mech, dilemma, 0)
                p_no_1 = mut_path("noshuffle", gs, mech, dilemma, 1)
                r_no_0 = load_con(p_no_0)
                r_no_1 = load_con(p_no_1)
                
                # Shuffle
                p_sh_0 = mut_path("shuffle", gs, mech, dilemma, 0)
                p_sh_1 = mut_path("shuffle", gs, mech, dilemma, 1)
                r_sh_0 = load_con(p_sh_0)
                r_sh_1 = load_con(p_sh_1)
                
                if not (r_no_0 and r_sh_0 and r_no_1 and r_sh_1):
                    continue
                
                # Noshuffle fraction
                no_0_map = {(round(float(r["c0"]), 4), round(float(r["c1"]), 4)): coop(r) for r in r_no_0}
                no_1_map = {(round(float(r["c0"]), 4), round(float(r["c1"]), 4)): coop(r) for r in r_no_1}
                no_greater = sum(1 for k in no_0_map if no_0_map.get(k, 0) > no_1_map.get(k, 0))
                no_frac = f"{no_greater}/{len(no_0_map)}"
                
                # Shuffle fraction
                sh_0_map = {(round(float(r["c0"]), 4), round(float(r["c1"]), 4)): coop(r) for r in r_sh_0}
                sh_1_map = {(round(float(r["c0"]), 4), round(float(r["c1"]), 4)): coop(r) for r in r_sh_1}
                sh_greater = sum(1 for k in sh_0_map if sh_0_map.get(k, 0) > sh_1_map.get(k, 0))
                sh_frac = f"{sh_greater}/{len(sh_0_map)}"
                
                print(f"{mech:10s} | {d_name:8s} | {gs:4s} | {no_frac:9s} | {sh_frac:9s}")
        print("-" * 55)

    # 3. Cooperation at Specific Asymmetries: Mild (0.1, 0.2) vs High (0.1, 0.3) for GS=128
    print("\n--- 3. SAMPLE CELL DETAILS (gs=128, fset_0 / fset_1) ---")
    print(f"{'Mechanism':10s} | {'Dilemma':8s} | Cond      | Cell (0.1, 0.2) | Cell (0.1, 0.3)")
    print("-" * 65)
    
    for mech in mechs:
        for dilemma in dilemmas:
            d_name = "PD (d1)" if dilemma == 1 else "SD (d2)"
            # Noshuffle
            p_no_0 = mut_path("noshuffle", "128", mech, dilemma, 0)
            p_no_1 = mut_path("noshuffle", "128", mech, dilemma, 1)
            r_no_0 = load_con(p_no_0)
            r_no_1 = load_con(p_no_1)
            
            # Shuffle
            p_sh_0 = mut_path("shuffle", "128", mech, dilemma, 0)
            p_sh_1 = mut_path("shuffle", "128", mech, dilemma, 1)
            r_sh_0 = load_con(p_sh_0)
            r_sh_1 = load_con(p_sh_1)
            
            if not (r_no_0 and r_sh_0 and r_no_1 and r_sh_1):
                continue
                
            no_0_map = {(round(float(r["c0"]), 4), round(float(r["c1"]), 4)): coop(r) for r in r_no_0}
            no_1_map = {(round(float(r["c0"]), 4), round(float(r["c1"]), 4)): coop(r) for r in r_no_1}
            sh_0_map = {(round(float(r["c0"]), 4), round(float(r["c1"]), 4)): coop(r) for r in r_sh_0}
            sh_1_map = {(round(float(r["c0"]), 4), round(float(r["c1"]), 4)): coop(r) for r in r_sh_1}
            
            # Noshuffle cells
            no_mild = f"{no_0_map.get((0.1, 0.2), 0.0):.3f} / {no_1_map.get((0.1, 0.2), 0.0):.3f}"
            no_high = f"{no_0_map.get((0.1, 0.3), 0.0):.3f} / {no_1_map.get((0.1, 0.3), 0.0):.3f}"
            
            # Shuffle cells
            sh_mild = f"{sh_0_map.get((0.1, 0.2), 0.0):.3f} / {sh_1_map.get((0.1, 0.2), 0.0):.3f}"
            sh_high = f"{sh_0_map.get((0.1, 0.3), 0.0):.3f} / {sh_1_map.get((0.1, 0.3), 0.0):.3f}"
            
            print(f"{mech:10s} | {d_name:8s} | noshuffle | {no_mild}   | {no_high}")
            print(f"{'':10s} | {'':8s} | shuffle   | {sh_mild}   | {sh_high}")
            print("-" * 65)

if __name__ == "__main__":
    main()
