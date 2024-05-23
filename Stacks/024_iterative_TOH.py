import stack_functions as sf

def create_stack(n):
    return [None] * n, -1

def moveDisk(fromPole, toPole, disc):
    print(f"Move disk {disc} from pole {fromPole} to pole {toPole}.")

def moveDiskBetweenPoles(src, dest, s, d):
    s_stack, s_top = src[0], src[1]
    d_stack, d_top = dest[0], dest[1]

    if sf.isEmpty(s_top): # Source stack is empty
        moveDisk(d, s, d_stack[d_top])
    elif sf.isEmpty(d_top) or s_stack[s_top] < d_stack[d_top]:
        d_top, X, d_stack = sf.pop(d_stack, d_top)
        s_top, s_stack = sf.push(s_stack, s_top, X)
        moveDisk(s, d, X)
    else:
        s_top, X, s_stack = sf.pop(s_stack, s_top)
        d_top, d_stack = sf.push(d_stack, d_top, X)
        moveDisk(d, s, X)

def tohIterative(num_discs, S, A, D):
    s = 'S'
    a = 'A'
    d = 'D'

    if num_discs == 1:
        moveDisk(s, d, num_discs)
    else:
        if num_discs % 2 == 0:
            a, d = d, a

        for disc in range(num_discs, 0, -1):
            S[1], S[0] = sf.push(S[0], S[1], disc)
            

        print("SOURCE STACK: \n")
        sf.display_stack(S[0], S[1])
        print("\n")
        total_moves = 2 ** num_discs - 1
        for move in range(total_moves):
            print(f"{move} % {num_discs} = {move % num_discs}")

N = int(input("Enter the number of discs: "))

src, src_TOP = create_stack(N)
aux, aux_TOP = create_stack(N)
dest, dest_TOP = create_stack(N)

source = [src, src_TOP]
auxillary = [aux, aux_TOP]
destination = [dest, dest_TOP]

tohIterative(N, source, auxillary, destination)
