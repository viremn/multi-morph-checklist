def get_answer_variations(data, lang=None, task=None):
    if lang is None:
        lang = data['lang']
    if task is None:
        task = data['task']
    
    if task == 'negation1':
        if lang == 'en':
            answer_variations = en_negation(data)
        elif lang == 'de':
            answer_variations = de_negation(data)
        elif lang == 'fi':
            answer_variations = fi_negation(data)
        elif lang == 'ja':
            answer_variations = ja_negation1(data)
    elif task == 'negation2':
        if lang == 'en':
            answer_variations = en_negation(data)
        elif lang == 'de':
            answer_variations = de_negation(data)
        elif lang == 'fi':
            answer_variations = fi_negation(data)
        elif lang == 'ja':
            answer_variations = ja_negation2(data)
    elif task == 'numerals1':
        if lang == 'en':
            answer_variations = en_numerals1(data)
        elif lang == 'de':
            answer_variations = de_numerals1(data)
        elif lang == 'fi':
            answer_variations = fi_numerals1(data)
        elif lang == 'ja':
            answer_variations = ja_numerals1(data)
    elif task == 'numerals2':
        if lang == 'en':
            answer_variations = en_numerals2(data)
        elif lang == 'de':
            answer_variations = de_numerals2(data)
        elif lang == 'fi':
            answer_variations = fi_numerals2(data)
        elif lang == 'ja':
            answer_variations = ja_numerals2(data)
    elif task == 'numerals2':
        if lang == 'en':
            pass
        elif lang == 'de':
            pass
        elif lang == 'fi':
            pass
        elif lang == 'ja':
            pass
    elif task == 'spatial1':
        if lang == 'en':
            pass
        elif lang == 'de':
            pass
        elif lang == 'fi':
            pass
        elif lang == 'ja':
            pass
    elif task == 'spatial2':
        if lang == 'en':
            pass
        elif lang == 'de':
            pass
        elif lang == 'fi':
            pass
        elif lang == 'ja':
            pass
    elif task == 'temporal1':
        if lang == 'en':
            pass
        elif lang == 'de':
            pass
        elif lang == 'fi':
            pass
        elif lang == 'ja':
            pass
    elif task == 'temporal2':
        if lang == 'en':
            pass
        elif lang == 'de':
            pass
        elif lang == 'fi':
            pass
        elif lang == 'ja':
            pass
    elif task == 'comparative1':
        if lang == 'en':
            pass
        elif lang == 'de':
            pass
        elif lang == 'fi':
            pass
        elif lang == 'ja':
            pass
    elif task == 'comparative2':
        if lang == 'en':
            pass
        elif lang == 'de':
            pass
        elif lang == 'fi':
            pass
        elif lang == 'ja':
            pass
    elif task == 'zh_ja_counters':
        if lang == 'ja':
            pass

def en_negation(data):

    # POSITIVES
    # Mark and Andrew
    # Andrew and Mark
    # Mark and Andrew are doctors
    # Andrew and Mark are doctors

    # NEGATIVES
    # Mark and Andrew
    # Andrew and Mark
    # Mark and Andrew are not doctors
    # Andrew and Mark are not doctors
    # Emma and Monica are doctors
    # Monica and Emma are doctors

    conj = ' and '

    subjects = data['answer'].strip('.')
    subjects = [subjects, conj.join(subjects.split(conj)[::-1])] if conj in subjects else [subjects]
    predicate = ' '.join(data['question'].strip('?').split(' ')[1:])
    non_subjects = data['context'].split(' ')
    non_subjects = ' '.join(non_subjects[:3]) if conj.strip() in non_subjects[:3] else ' '.join(non_subjects[:1])
    non_subjects = [non_subjects, conj.join(non_subjects.split(conj)[::-1])] if conj in non_subjects else [non_subjects]

    perfect_matches = subjects
    positive_matches = [subject + ' ' + predicate for subject in subjects]
    negative_matches = [subject + ' ' + predicate for subject in non_subjects]

    return {'perfect': perfect_matches, 
            'positive': positive_matches,
            'negative': negative_matches}

def de_negation(data):
    conj = ' und '

    subjects = data['answer'].strip('.')
    subjects = [subjects, conj.join(subjects.split(conj)[::-1])] if conj in subjects else [subjects]
    predicate = ' '.join(data['question'].strip('?').split(' ')[1:])
    non_subjects = data['context'].split(' ')
    non_subjects = ' '.join(non_subjects[:3]) if conj.strip() in non_subjects[:3] else ' '.join(non_subjects[:1])
    non_subjects = [non_subjects, conj.join(non_subjects.split(conj)[::-1])] if conj in non_subjects else [non_subjects]

    perfect_matches = subjects
    positive_matches = [subject + ' ' + predicate for subject in subjects]
    negative_matches = [subject + ' ' + predicate for subject in non_subjects]
    
    return {'perfect': perfect_matches, 
            'positive': positive_matches,
            'negative': negative_matches}

def fi_negation(data):
    conj = ' ja '

    subjects = data['answer'].strip('.')
    subjects = [subjects, conj.join(subjects.split(conj)[::-1])] if conj in subjects else [subjects]
    predicate = ' '.join(data['question'].strip('?').split(' ')[1:])
    non_subjects = data['context'].split(' ')
    non_subjects = ' '.join(non_subjects[:3]) if conj.strip() in non_subjects[:3] else ' '.join(non_subjects[:1])
    non_subjects = [non_subjects, conj.join(non_subjects.split(conj)[::-1])] if conj in non_subjects else [non_subjects]

    perfect_matches = subjects
    positive_matches = [subject + ' ' + predicate for subject in subjects]
    negative_matches = [subject + ' ' + predicate for subject in non_subjects]

    return {'perfect': perfect_matches, 
            'positive': positive_matches,
            'negative': negative_matches}

def ja_negation1(data):
    conj = 'と'
    cop = 'でございます' if data['answer'].endswith('でございます。') else 'です' if data['answer'].endswith('です。') else ''

    subjects = data['answer'].strip('。')[:-len(cop)] if cop != '' else data['answer'].strip('。 ')
    subjects = [subjects, conj.join(subjects.split(conj)[::-1])] if conj in subjects else [subjects]

    predicate = ' '.join(data['question'].rstrip('か。？?').split('が')[1:])
    predicate = predicate[:-len(cop)] if cop != '' else predicate

    non_subjects = data['context'].split('は')[0]
    non_subjects = [non_subjects, conj.join(non_subjects.split(conj)[::-1])] if conj in non_subjects else [non_subjects]

    perfect_matches = []
    positive_matches = []
    negative_matches = []
    for subject in subjects:
        if cop == '':
            perfect_matches.append(f"{subject}")
            perfect_matches.append(f"{subject}だ")

            positive_matches.append(f"{subject}が{predicate}")
            positive_matches.append(f"{subject}が{predicate}だ")

            positive_matches.append(f"{predicate}は{subject}")
            positive_matches.append(f"{predicate}は{subject}だ")
        elif cop == 'です':
            perfect_matches.append(f"{subject}です")

            positive_matches.append(f"{subject}が{predicate}です")

            positive_matches.append(f"{predicate}は{subject}です")
        elif cop == 'でございます':
            perfect_matches.append(f"{subject}でございます")

            positive_matches.append(f"{subject}が{predicate}でございます")

            positive_matches.append(f"{predicate}は{subject}でございます")

    for subject in non_subjects:
        if cop == '':
            negative_matches.append(f"{subject}が{predicate}")
            negative_matches.append(f"{subject}が{predicate}だ")

            negative_matches.append(f"{predicate}は{subject}")
            negative_matches.append(f"{predicate}は{subject}だ")
        elif cop == 'です':
            negative_matches.append(f"{subject}が{predicate}です")

            negative_matches.append(f"{predicate}は{subject}です")
        elif cop == 'でございます':
            negative_matches.append(f"{subject}が{predicate}でございます")

            negative_matches.append(f"{predicate}は{subject}でございます")

    return {'perfect': perfect_matches, 
            'positive': positive_matches,
            'negative': negative_matches}

def ja_negation2(data):
    conj = 'と'
    cop = 'でございます' if data['answer'].endswith('でございます。') else 'です' if data['answer'].endswith('です。') else ''

    subjects = data['answer'].strip('。')[:-len(cop)] if cop != '' else data['answer'].strip('。 ')
    subjects = [subjects, conj.join(subjects.split(conj)[::-1])] if conj in subjects else [subjects]

    predicate = data['question'].rstrip('か。？?').split('のは')[0].replace('じゃない', '').replace('でない', '')

    non_subjects = data['context'].split('は')[0]
    non_subjects = [non_subjects, conj.join(non_subjects.split(conj)[::-1])] if conj in non_subjects else [non_subjects]

    perfect_matches = []
    positive_matches = []
    negative_matches = []
    for subject in subjects:
        if cop == '':
            perfect_matches.append(f"{subject}")
            perfect_matches.append(f"{subject}だ")

            positive_matches.append(f"{subject}が{predicate}じゃない")
            positive_matches.append(f"{subject}が{predicate}ではない")

            positive_matches.append(f"{predicate}じゃないのは{subject}だ")
            positive_matches.append(f"{predicate}でないのは{subject}だ")

        elif cop == 'です':
            perfect_matches.append(f"{subject}です")

            positive_matches.append(f"{subject}が{predicate}じゃありません")
            positive_matches.append(f"{subject}が{predicate}ではありません")
            positive_matches.append(f"{subject}が{predicate}じゃないです")
            positive_matches.append(f"{subject}が{predicate}ではないです")

            positive_matches.append(f"{predicate}でないのは{subject}です")
            positive_matches.append(f"{predicate}じゃないのは{subject}です")

        elif cop == 'でございます':
            perfect_matches.append(f"{subject}でございます")

            positive_matches.append(f"{subject}が{predicate}ではございません")

            positive_matches.append(f"{predicate}でないのは{subject}でございます")

    for subject in non_subjects:
        if cop == '':
            negative_matches.append(f"{subject}")
            negative_matches.append(f"{subject}だ")

            negative_matches.append(f"{subject}が{predicate}じゃない")
            negative_matches.append(f"{subject}が{predicate}ではない")

            negative_matches.append(f"{predicate}じゃないのは{subject}だ")
            negative_matches.append(f"{predicate}でないのは{subject}だ")
            
        elif cop == 'です':
            negative_matches.append(f"{subject}です")

            negative_matches.append(f"{subject}が{predicate}じゃありません")
            negative_matches.append(f"{subject}が{predicate}ではありません")
            negative_matches.append(f"{subject}が{predicate}じゃないです")
            negative_matches.append(f"{subject}が{predicate}ではないです")

            negative_matches.append(f"{predicate}でないのは{subject}です")
            negative_matches.append(f"{predicate}じゃないのは{subject}です")

        elif cop == 'でございます':
            negative_matches.append(f"{subject}でございます")

            negative_matches.append(f"{subject}が{predicate}ではございません")

            negative_matches.append(f"{predicate}でないのは{subject}でございます")

    return {'perfect': perfect_matches,
            'positive': positive_matches,
            'negative': negative_matches}

def en_numerals1(data):
    conj = ' and '

    number = data['answer'].strip('.')
    target = 'fruits'

    non_targets = [data['context'].split(conj)[0].split(' ')[-1], data['context'].split(conj)[-1].split(' ')[1]]

    perfect_matches = [number]
    positive_matches = [f"{number} {target}"]
    negative_matches = non_targets

    return {'perfect': perfect_matches,
            'positive': positive_matches,
            'negative': negative_matches}

def en_numerals2(data):
    conj = ' and '

    number = data['answer'].strip('.')
    target = data['question'].split(' ')[2]

    non_targets = [data['context'].split(conj)[-1].split(' ')[1]]

    perfect_matches = [number]
    positive_matches = [f"{number} {target}"]
    negative_matches = non_targets

    return {'perfect': perfect_matches,
            'positive': positive_matches,
            'negative': negative_matches}

def de_numerals1(data):
    conj = ' und '

    number = data['answer'].strip('.')
    target = 'Früchte'

    non_targets = [data['context'].split(conj)[0].split(' ')[-1], data['context'].split(conj)[-1].split(' ')[1]]

    perfect_matches = [number]
    positive_matches = [f"{number} {target}"]
    negative_matches = non_targets

    return {'perfect': perfect_matches,
            'positive': positive_matches,
            'negative': negative_matches}

def de_numerals2(data):
    conj = ' und '

    number = data['answer'].strip('.')
    target = data['question'].split(' ')[2]

    non_targets = [data['context'].split(conj)[-1].split(' ')[1]]

    perfect_matches = [number]
    positive_matches = [f"{number} {target}"]
    negative_matches = non_targets

    return {'perfect': perfect_matches,
            'positive': positive_matches,
            'negative': negative_matches}

def fi_numerals1(data):
    conj = ' ja '

    number = data['answer'].strip('.')
    target = 'hedelmää'

    non_targets = [data['context'].split(conj)[0].split(' ')[-1], data['context'].split(conj)[-1].split(' ')[1].strip('.')]

    perfect_matches = [number]
    positive_matches = [f"{number} {target}"]
    negative_matches = non_targets

    return {'perfect': perfect_matches,
            'positive': positive_matches,
            'negative': negative_matches}

def fi_numerals2(data):
    conj = ' ja '

    number = data['answer'].strip('.')
    target = data['question'].split(' ')[2]

    non_targets = [data['context'].split(conj)[-1].split(' ')[1].strip('.')]

    perfect_matches = [number]
    positive_matches = [f"{number} {target}"]
    negative_matches = non_targets

    return {'perfect': perfect_matches,
            'positive': positive_matches,
            'negative': negative_matches}

def ja_numerals1(data):
    number, cop = data['answer'].strip('。').split('個')

    non_targets = [data['context'].split('個の')[1].split('と')[0], 
                data['context'].split('個の')[-1].split('が')[0]]

    perfect_matches = [data['answer'].strip('。 ')]
    positive_matches = [f'{number}個']
    negative_matches = non_targets

    return {'perfect': perfect_matches,
        'positive': positive_matches,
        'negative': negative_matches}

def ja_numerals2(data):
    number = data['answer'].strip('。').split('個')[0]

    non_targets = [data['context'].split('個の')[2].split('が')[0]]

    perfect_matches = [data['answer'].strip('。 ')]
    positive_matches = [f'{number}個']
    negative_matches = non_targets

    return {'perfect': perfect_matches,
        'positive': positive_matches,
        'negative': negative_matches}