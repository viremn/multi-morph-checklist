import json

def load_responses(data, quota, langs, tasks):
    loaded_responses = {f"{lang}_{task}": [] for lang in langs for task in tasks}
    for id, item in data.items():
        if item['lang'] in langs and item['task'] in tasks:
            if not 'human_eval' in item.keys() and len(loaded_responses[f"{item['lang']}_{item['task']}"]) < quota:
                loaded_responses[f"{item['lang']}_{item['task']}"].append((id, item))
    return loaded_responses

def save_progress(data):
    print('SAVING...')
    json.dump(data, open('/home/norrman/GitHub/multi-morph-checklist/M2C_xglm_responses_human_evaluated.json', 'w'), indent=4)
    print('SAVE SUCCESSFUL!')

def check_neg_prototypical(item, response):
    prototypical = {
                        'en_spatial2': {'keys': (), 
                                        'sents': []},
                        'en_temporal1': {'keys': (), 
                                        'sents': []},
                        'en_temporal2': {'keys': (), 
                                        'sents': [],},
                        'en_comparative1': {'keys': ('P1', 'N1', 'N2', 'P2'), 
                                        'sents': ['N1 is N2 than P1',
                                                  'N1 is P2 than P1',
                                                  'P1 is N2',
                                                  'P1 is N2 than N1'],},
                        
                        'de_spatial2': {'keys': (), 
                                        'sents': []},
                        'de_temporal1': {'keys': (), 
                                        'sents': []},
                        'de_temporal2': {'keys': (), 
                                        'sents': [],},
                        'de_comparative1': {'keys': (), 
                                        'sents': [],},
                        'ja_fam_comparative1': {'keys': ('P1', 'P2', 'N1', 'N2'), 
                                        'sents': ['P1はN2だ',
                                                  'P1はN2',
                                                  'N1はP1よりN2だ',
                                                  'N1はP1よりN2',
                                                  'P1は、N2だ',
                                                  'P1は、N2',
                                                  'N1は、P1よりN2だ',
                                                  'N1は、P1よりN2',
                                                  'P1よりN2']}, 
                        'ja_fam_comparative2': {'keys': ('P1', 'P2', 'N1', 'N2'), 
                                        'sents': []},

                    }
    
    if f"{item['lang']}_{item['task']}" in prototypical:
        response = response.lower().strip()
        for target in prototypical[f"{item['lang']}_{item['task']}"]['keys']:
            if not target in item['targets']:
                sub_targets = [t for t in item['targets'].keys() if t.startswith(target)]
                for t in sub_targets:
                    response = response.replace(item['targets'][t], t)
            else:
                response = response.replace(item['targets'][target], target)
        print('NEG PROTOTYPICAL:', response)
        return response in prototypical[f"{item['lang']}_{item['task']}"]['sents']
    return False

def check_prototypical(item, response):
    prototypical = {
                        'en_spatial2': {'keys': ('P1', 'P2'), 
                                        'sents': ['the P2 is P1',
                                                  'the P2 are P1']},
                        'en_temporal1': {'keys': ('P1', 'P2'), 
                                        'sents': ['P1 is a P2',
                                                  'P1 is an P2']},
                        'en_temporal2': {'keys': ('P1', 'P2'), 
                                        'sents': ['P1 will be a P2',
                                                  'P1 will be an P2'],},
                        'en_comparative1': {'keys': ('P1', 'P2', 'N1'), 
                                        'sents': ['P1 is P2',
                                                  'P1 is P2 than N1'],},
                        'en_comparative2': {'keys': ('P1', 'P2', 'N1'), 
                                        'sents': []},
                        
                        
                        'de_negation1': {'keys': ('P1', 'P2'), 
                                        'sents': ['P1 ist P2',
                                                  'P1A und P1B sind P2',
                                                  'P1 ist ein P2',
                                                  'P1 ist eine P2',]},
                        'de_negation2': {'keys': ('P1'), 
                                        'sents': []},
                        'de_numerals1': {'keys': ('P1'), 
                                        'sents': []},
                        'de_numerals2': {'keys': ('P1'), 
                                        'sents': []},
                        'de_spatial1': {'keys': ('P1'), 
                                        'sents': []},
                        'de_spatial2': {'keys': ('P1'), 
                                        'sents': []},
                        'de_temporal1': {'keys': ('P1'), 
                                        'sents': []},
                        'de_temporal2': {'keys': ('P1'), 
                                        'sents': [],},
                        'de_comparative1': {'keys': ('P1'), 
                                        'sents': [],},
                        'de_comparative2': {'keys': ('P1'), 
                                        'sents': []},
                        'ja_fam_spatial2': {'keys': ('P1', 'P2'), 
                                        'sents': ['P2はP1だ',
                                                  'P1だ',
                                                  'P1に置いてある',
                                                  'P1に置いた',
                                                  'P1にある',
                                                  'P2は、P1だ']},
                        'ja_fam_temporal1': {'keys': ('P1', 'P2'), 
                                        'sents': ['P1はP2だ',
                                                  'P2はP1だ',
                                                  'P1はP2',
                                                  'P2はP1',
                                                  'P1は転職して今はP2',
                                                  'P1は転職して今はP2だ',
                                                  'P1は、P2だ',
                                                  'P1は、P1だ',
                                                  'P1は、P2',
                                                  'P1は、転職して今はP2',
                                                  'P1は、転職して今はP2だ',
                                                  'P1は、P2の資格を持っている',
                                                  ]},
                        'ja_fam_temporal2': {'keys': ('P1', 'P2', 'N1', 'N2'), 
                                        'sents': ['P1は転職してP2になる',
                                                  'P1は、転職してP2になる',
                                                  'P1は、P2の仕事に就く',
                                                  'P1はP2の仕事に就く',
                                                  'P1は、P2になる',
                                                  'P1はP2になる',
                                                  'P1は、P2の資格を持っている'
                                                  ]},
                        'ja_fam_comparative1': {'keys': ('P1', 'P2', 'N1', 'N2'), 
                                        'sents': ['P1はP2だ',
                                                  'P1はP2',
                                                  'P1はN1よりP2だ',
                                                  'P1はN1よりP2',
                                                  'P1は、P2だ',
                                                  'P1は、P2',
                                                  'P1は、N1よりP2だ',
                                                  'P1は、N1よりP2',]},
                        'ja_fam_comparative2': {'keys': ('P1', 'P2', 'N1', 'N2'), 
                                        'sents': []},
                                                                         
                    }
    
    if f"{item['lang']}_{item['task']}" in prototypical:
        response = response.lower().strip()
        for target in prototypical[f"{item['lang']}_{item['task']}"]['keys']:
            if not target in item['targets']:
                sub_targets = [t for t in item['targets'].keys() if t.startswith(target)]
                for t in sub_targets:
                    response = response.replace(item['targets'][t], t)
            else:
                response = response.replace(item['targets'][target], target)
            
        print('PROTOTYPICAL:', response)
        return response in prototypical[f"{item['lang']}_{item['task']}"]['sents']
    return False
    
if __name__ == '__main__':
    with open('/home/norrman/GitHub/multi-morph-checklist/M2C_xglm_responses_human_evaluated.json', 'r') as f:
        data = json.load(f)

    langs = [
            #  'en', 
            #  'de', 
            #  'fi', 
             'ja_fam', 
            #  'ja_norm', 
            #  'ja_form'
             ]
    tasks = [
            #  'negation1',
            #  'negation2',
            #  'numerals1',
            #  'numerals2',
            #  'spatial1',
            #  'spatial2',
            #  'temporal1',
            #  'temporal2',
            #  'comparative1',
             'comparative2',
             'counters'
             ]

    quota = 100

    loaded_items = load_responses(data, quota, langs, tasks)

    num_items = len([response for item_list in loaded_items.values() for id, item in item_list for response in item['response'].values()])
    curr_item = 0
    to_save = False
    for lang_task, item_list in loaded_items.items():
        print('STARTING EVALUATION:', lang_task)
        for id, item in item_list:
            human_eval = {}
            for model, response in item['response'].items():
                curr_item += 1
                print(f"Response {curr_item} out of {num_items}. Current ID: {id}")
                print('Context:', item['context'])
                print('Question:', item['question'])
                print('Answer:', item['answer'])
                print()
                trimmed_response = response.split('.')[0] if 'ja' not in item['lang'] else response.split('。')[0]
                print('Response:', trimmed_response)
                if trimmed_response.lower() == item['answer'][:-1].lower():
                    print('FOUND PERFECT MATCH.')
                    command = 'c' 
                elif item['task'] in ['negation1', 'negation2', 'spatial1', 'temporal1', 'temporal2'] and trimmed_response.lower() == item['context'][:-1].lower():
                    print('FOUND CONTEXT RESPONSE.')
                    command = 'c'
                elif check_prototypical(item, trimmed_response):
                    print('FOUND PROTOTYPICAL RESPONSE.')
                    command = 'c'
                elif check_neg_prototypical(item, trimmed_response):
                    print('FOUND NEGATIVE PROTOTYPICAL.')
                    command = 'n'
                elif not item['hit_targets'][model]['P1']:
                    print('PRIMARY TARGET NOT IN RESPONSE.')
                    command = 'n'

                else: command = ''
                while command not in {'c', 'n'}:
                    command = input('Enter "c" if the response is correct, else "n".').lower()
                    if command == 'save':
                        save_progress(data)
                    elif command == 'exit':
                        save_progress(data)
                        print('EXITING...')
                        exit()
                human_eval[model] = command == 'c'
                print()
            item['human_eval'] = human_eval
        print('COMPLETED:', lang_task)
        save_progress(data)

    save_progress(data)
    print('EXITING...')