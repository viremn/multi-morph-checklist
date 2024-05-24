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
            pass
    elif task == 'numerals1':
        if lang == 'en':
            pass
        elif lang == 'de':
            pass
        elif lang == 'fi':
            pass
        elif lang == 'ja':
            pass
    elif task == 'numerals2':
        if lang == 'en':
            pass
        elif lang == 'de':
            pass
        elif lang == 'fi':
            pass
        elif lang == 'ja':
            pass
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