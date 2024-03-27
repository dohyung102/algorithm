def solution(sequence):
    answer = 0
    sequence_length = len(sequence)
    pulse = [(-1) ** idx for idx in range(sequence_length)]
    pulse_sequence = list(i * j for i, j in zip(sequence, pulse))
    sum_pulse_sequence = 0
    for idx in range(sequence_length):
        sum_pulse_sequence += pulse_sequence[idx]
        if abs(answer) < abs(sum_pulse_sequence + answer):
            answer += sum_pulse_sequence
            sum_pulse_sequence = 0
        elif abs(answer) < abs(sum_pulse_sequence):
            answer = sum_pulse_sequence
            sum_pulse_sequence = 0
    answer = abs(answer)
    return answer