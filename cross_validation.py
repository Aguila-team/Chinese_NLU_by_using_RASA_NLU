import copy
import json

from joblib import Parallel, delayed

from rasa_nlu.evaluate import (
    run_cv_evaluation,
    training_data,
    drop_intents_below_freq,
    config
)

from config import pipeline_registry


def cross_validation(data_path, config_path):
    # same as rasa_nlu's evaluate interface
    data = training_data.load_data(data_path)
    data = drop_intents_below_freq(data, cutoff=5)

    # same as rasa_nlu's evaluate interface
    default_folds = 10

    # same as rasa_nlu's evaluate interface
    nlu_config = config.load(config_path)

    intent_results, entity_results = run_cv_evaluation(data, default_folds,
                                                       nlu_config)

    template_result = {
        'intent': {
            'train': {},
            'test': {}
        },
        'entity': {
            'train': {},
            'test': {}
        },
    }

    set_template_result(intent_results.train,
                        template_result['intent']['train'])
    set_template_result(intent_results.test, template_result['intent']['test'])

    set_template_result(entity_results.train.values()[0],
                        template_result['entity']['train'])
    set_template_result(entity_results.test.values()[0],
                        template_result['entity']['test'])

    return template_result


def set_template_result(raw_result, template_sub_result):
    for k, v in raw_result:
        key = get_template_key(k)
        template_sub_result[key] = v


def get_template_key(key):
    # mapping original rasa_nlu result key to keys used in README template
    key_mapping = {}

    only_case_different_key = []
    case_mapping = {i: i.upper() for i in only_case_different_key}
    key_mapping.update(case_mapping)

    special_case_mapping = {
    }
    key_mapping.update(special_case_mapping)

    if key in key_mapping:
        return key_mapping[key]
    else:
        # default case, return uppercase of key
        return key.upper()


def sequence_process():
    template_variable = []

    for pipeline in pipeline_registry:
        pipeline_variable = process_pipeline(pipeline)

        template_variable.append(pipeline_variable)

    return template_variable


def parallel_process():
    return Parallel(n_jobs=-1)(delayed(process_pipeline)(i) for i in pipeline_registry)


def process_pipeline(pipeline):
    pipeline_variable = copy.deepcopy(pipeline)

    result = cross_validation(
        pipeline['settings']['data_path'],
        pipeline['settings']['config_path']
    )

    # adding other items that will be used
    pipeline_variable['result'] = result

    return pipeline_variable


def main():
    template_variable = parallel_process()

    with open("result.json") as fd:
        json.dump(template_variable, fd)


if __name__ == "__main__":
    main()
