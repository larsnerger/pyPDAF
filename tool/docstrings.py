"""Generate API docstrings for pyPDAF functions
"""
from pdaf_assimilate_docstrings import docstrings as assimilate_docstrings
from pdaf_diag_docstrings import docstrings as diag_docstrings
from pdaf_put_state_docstrings import docstrings as put_state_docstrings
from pdaflocal_assimilate_docstrings import docstrings as local_assimilate_docstrings
from pdaflocalomi_assimilate_docstrings import docstrings as localomi_assimilate_docstrings
from pdaflocalomi_put_state_docstrings import docstrings as localomi_put_state_docstrings
from pdafomi_assimilate_docstrings import docstrings as omi_assimilate_docstrings
from pdafomi_put_state_docstrings import docstrings as omi_put_state_docstrings

docstrings = {**assimilate_docstrings, **diag_docstrings, **
              put_state_docstrings, **local_assimilate_docstrings, **
              localomi_assimilate_docstrings, **localomi_put_state_docstrings,
              **omi_assimilate_docstrings, **omi_put_state_docstrings}


docstrings['deallocate'] = \
    "Finalise the PDAF systems\n    " \
    "including freeing some of\n    " \
    "the memory used by PDAF.\n\n    " \
    "This function cannot be used to\n    " \
    "free all allocated PDAF memory.\n    " \
    "Therefore, one should not use\n    " \
    ":func:`pyPDAF.PDAF.init` afterwards."

docstrings['eofcovar'] = \
    "EOF analysis of an ensemble of state vectors " \
    "by singular value decomposition.\n\n    " \
    "Typically, this function is used with" \
    "\n    " \
    ":func:`pyPDAF.PDAF.SampleEns`\n    " \
    "to generate an ensemble of a chosen size \n    " \
    "(up to the number of EOFs plus one).\n\n    " \
    "Here, the function performs a singular value decomposition" \
    "\n    " \
    "of the ensemble anomaly of the input matrix,\n    " \
    "which is usually an ensemble formed by state vectors" \
    "\n    " \
    "at multiple time steps.\n    " \
    "The singular values and corresponding singular vectors" \
    "\n    " \
    "can be used to\n    " \
    "construct a covariance matrix.\n    " \
    "This can be used as the initial error covariance" \
    "\n    " \
    "for the initial ensemble.\n\n    " \
    "A multivariate scaling can be performed to ensure that " \
    "all fields in the state vectors have unit variance.\n\n    " \
    "It can be useful to store more EOFs than one finally\n    " \
    "might want to use to have the flexibility\n    " \
    "to carry the ensemble size.\n\n\n    " \
    "See Also\n    " \
    "--------\n    " \
    "`PDAF webpage <https://pdaf.awi.de/trac/wiki/EnsembleGeneration>`_"

docstrings['gather_dim_obs_f'] = \
    "Gather the dimension of observation vector\n    " \
    "across multiple local domains/filter processors.\n\n    " \
    "This function is typically used in deprecated PDAF functions" \
    "\n    " \
    "without OMI.\n\n    " \
    "This function can be used in the user-supplied function of" \
    "\n    " \
    ":func:`py__init_dim_obs_f_pdaf`,\n    " \
    "but it is recommended to use :func:`pyPDAF.PDAF.omi_gather_obs`" \
    "\n    " \
    "with OMI.\n\n    " \
    "This function does two things:\n    " \
    "    1. Receiving observation dimension on each local process." \
    "\n    " \
    "    2. Gather the total dimension of observation\n    " \
    "       across local process and the displacement of PE-local" \
    "\n    " \
    "       observations relative to the total observation vector" \
    "\n\n    " \
    "The dimension of observations are used to allocate observation" \
    "\n    " \
    "arrays. Therefore, it must be used before\n    " \
    ":func:`pyPDAF.PDAF.gather_obs_f` or\n    " \
    ":func:`pyPDAF.PDAF.gather_obs_f2`."

docstrings['gather_obs_f'] = \
    "In the local filters (LESKTF, LETKF, LSEIK, LNETF) " \
    "this function returns the total observation vector " \
    "from process-local observations. " \
    "The function depends on " \
    "`pyPDAF.PDAF.gather_dim_obs_f` which defines the process-local observation dimensions. " \
    "Further, the related routine `pyPDAF.PDAF.gather_obs_f2` is used to\n    " \
    "gather the associated 2D observation coordinates\n    "

docstrings['gather_obs_f2'] = \
    "In the local filters (LESKTF, LETKF, LSEIK, LNETF)\n    " \
    "this function returns the full observation coordinates " \
    "from process-local observation coordinates. " \
    "The function depends on " \
    "`pyPDAF.PDAF.gather_dim_obs_f` which defines the process-local observation dimensions. " \
    "Further, the related routine `pyPDAF.PDAF.gather_obs_f` is used to " \
    "gather the associated observation vectors. \n    \n    " \
    "The routine is typically used in the routines `py__init_dim_obs_f_pdaf` " \
    "if the analysis step of the local filters is parallelized."

docstrings['get_assim_flag'] = \
    "Return the flag that\n    " \
    "indicates if the DA is performed in the last time step.\n    " \
    "It only works for online DA systems. "

docstrings['get_ensstats'] = \
    "Return the skewness and kutosis used in LKNETF. "

docstrings['get_localfilter'] = \
    "Return whether a local filter is used. "

docstrings['get_memberid'] = \
    "Return the ensemble member id on the current process.\n\n    " \
    "For example, it can be called during the ensemble\n    " \
    "integration if ensemble-specific forcing is read.\n    " \
    "It can also be used in the user-supplied functions\n    " \
    "such as :func:`py__collect_state_pdaf` and\n    " \
    ":func:`py__distribute_state_pdaf`."

docstrings['get_obsmemberid'] = \
    "Return the ensemble member id\n    " \
    "when observation operator is being applied.\n\n    " \
    "This function is used specifically for\n    " \
    "user-supplied function :func:`py__obs_op_pdaf`."

docstrings['get_smootherens'] = \
    "Return the smoothed ensemble in earlier time steps.\n\n    " \
    "It is only used when the smoother options is used ."

docstrings['get_state'] = \
    "Distribute analysis state vector to an array.\n\n    " \
    "The primary purpose of this function is to distribute\n    " \
    "the analysis state vector to the model.\n    " \
    "This is attained by the user-supplied function\n    " \
    ":func:`py__distribute_state_pdaf`.\n    " \
    "One can also use this function to get the state vector\n    " \
    "for other purposes, e.g. to write the state vector to a file." \
    "\n\n    " \
    "In this function, the user-supplied function\n    " \
    ":func:`py__next_observation_pdaf` is executed\n    " \
    "to specify the number of forecast time steps\n    " \
    "until the next assimilation step.\n    " \
    "One can also use the user-supplied function to\n    " \
    "end the assimilation.\n\n    " \
    "In an online DA system, this function also execute\n    " \
    "the user-supplied function :func:`py__prepoststep_state_pdaf`," \
    "\n    " \
    "when this function is first called. The purpose of this design" \
    "\n    " \
    "is to call this function right after :func:`pyPDAF.PDAF.init`" \
    "\n    " \
    "to process the initial ensemble before using it to\n    " \
    "initialse model forecast. This user-supplied function\n    " \
    "will not be called afterwards.\n\n    " \
    "This function is also used in flexible parallel system\n    " \
    "where the number of ensemble members are greater than\n    " \
    "the parallel model tasks. In this case, this function\n    " \
    "is called multiple times to distribute the analysis ensemble." \
    "\n\n    " \
    "User-supplied function are executed in the following sequence:" \
    "\n\n    " \
    "    1. py__prepoststep_state_pdaf\n    " \
    "       (only in online system when first called)\n    " \
    "    2. py__distribute_state_pdaf\n    " \
    "    3. py__next_observation_pdaf"

docstrings['init'] = \
    "Initialise the PDAF system.\n\n    " \
    "It is called once at the beginning of the assimilation.\n\n    " \
    "The function specifies the type of DA methods,\n    " \
    "parameters of the filters, the MPI communicators,\n    " \
    "and other parallel options.\n    " \
    "The filter options including `filtertype`, `subtype`,\n    " \
    "`param_int`, and `param_real`\n    " \
    "are introduced in\n    " \
    "`PDAF filter options wiki page" \
    " <https://pdaf.awi.de/trac/wiki/AvailableOptionsforInitPDAF>`_." \
    "\n    " \
    "Note that the size of `param_int` and `param_real` depends on" \
    "\n    " \
    "the filter type and subtype. However, for most filters,\n    " \
    "they require at least the state vector size and ensemble size" \
    "\n    " \
    "for `param_int`, and the forgetting factor for `param_real`." \
    "\n\n    " \
    "The MPI communicators asked by this function depends on\n    " \
    "the parallelisation strategy.\n    " \
    "For the default parallelisation strategy, the user\n    " \
    "can use the parallelisation module\n    " \
    "provided under in `example directory " \
    "<https://github.com/yumengch/pyPDAF/blob/main/example>`_\n    " \
    "without modifications.\n    " \
    "The parallelisation can differ based on online and offline cases.\n    " \
    "Users can also refer to `parallelisation documentation " \
    "<https://yumengch.github.io/pyPDAF/parallel.html>`_ for\n    " \
    "explanations or modifications.\n\n    " \
    "This function also asks for a user-supplied function\n    " \
    ":func:`py__init_ens_pdaf`.\n    " \
    "This function is designed to provides an initial ensemble\n    " \
    "to the internal PDAF ensemble array.\n    " \
    "The internal PDAF ensemble then can be distributed to\n    " \
    "initialise the model forecast using\n    " \
    ":func:`pyPDAF.PDAF.get_state`.\n    " \
    "This user-supplied function can be empty if the model\n    " \
    "has already read the ensemble from restart files." \


docstrings['local_weight'] = \
    "Get localisation weight for given distance,\n    " \
    "cut-off radius, support radius, weighting type,\n    " \
    "and weighting function.\n\n    " \
    "This function is used in the analysis step of a filter\n    " \
    "to computes a localisation weight.\n\n    " \
    "Typically, in domain-localised filters, the function\n    " \
    "is called in user-supplied :func:`py__prodRinvA_l_pdaf`.\n    " \
    "In LEnKF, this function is called\n    " \
    "in user-supplied :func:`py__localize_covar_pdaf`.\n\n    " \
    "This function is usually only used without PDAF-OMI."

docstrings['print_info'] = \
    "Print the wallclock time and memory measured by PDAF.\n\n    " \
    "This should be called at the end of the DA program."

docstrings['reset_forget'] = \
    "Reset the forgetting factor manually\n    " \
    "during the assimilation process.\n\n    " \
    "For the local ensemble Kalman filters\n    " \
    "the forgetting factor can be set either globally\n    " \
    "if this function is called outside of the loop over\n    " \
    "local domains,\n    " \
    "or\n    " \
    "the forgetting factor can be set differently\n    " \
    "for each local analysis domain within the loop over\n    " \
    "local domains.\n\n    " \
    "For the LNETF and the global filters\n    " \
    "only a global setting of the forgeting factor is possible.\n    " \
    "In addition, the implementation of adaptive choices\n    " \
    "for the forgetting factor (beyond what is implemented in PDAF) are possible."

docstrings['SampleEns'] = \
    "Generate an ensemble from singular values and\n    " \
    "their vectors (EOF modes) of an ensemble anomaly matrix.\n\n    " \
    "The singular values and vectors are derived from\n    " \
    "the ensemble anomalies. This ensemble anomaly can be\n    " \
    "obtained from a time anomaly of a model trajectory using\n    " \
    ":func:`pyPDAF.PDAF.eofcovar`."

docstrings['set_debug_flag'] = \
    "Activate the debug output of the PDAF.\n\n    " \
    "Starting from the use of this function,\n    " \
    "the debug infomation is sent to screen output.\n    " \
    "The screen output end when the debug flag is\n    " \
    "set to 0 by this function.\n\n    " \
    "For the sake of simplicity,\n    " \
    "we recommend using debugging output for\n    " \
    "a single local domain, e.g.\n    " \
    "`if domain_p == 1: pyPDAF.PDAF.set_debug_flag(1)`"

docstrings['set_ens_pointer'] = \
    "Return the ensemble in a numpy array.\n\n    " \
    "Here the internal array data has the same memoery address\n    " \
    "as PDAF ensemble array allowing for manual ensemble modification."

docstrings['set_smootherens'] = \
    "Get a pointer to smoother ensemble.\n\n    " \
    "When smoother is used, the smoothed ensemble states\n    " \
    "at earlier times are stored in an internal array of PDAF.\n    " \
    "To be able to smooth post times,\n    " \
    "the smoother algorithm must have access to the past ensembles.\n\n    " \
    "In this function, the user can obtain a numpy array of\n    " \
    "smoother ensemble. This array has the same memory address\n    " \
    "as the internal PDAF smoother ensemble array.\n    " \
    "This allows for manual modification of the smoother ensemble.\n\n    " \
    "In the offline mode the user has to manually\n    " \
    "fill the smoother ensemble array\n    " \
    "from ensembles read in from files.\n    " \
    "This function is typically called in\n    " \
    ":func:`py__init_ens_pdaf` in the call to\n    " \
    ":func:`pyPDAF.PDAF.PDAF_init`.\n\n    " \
    "In the online mode, the smoother array is filled\n    " \
    "automatically during the cycles of forecast phases and analysis steps."

docstrings['seik_TtimesA'] = \
    "Perform matrix calculation of B = TA.\n\n    " \
    "In this function, the input matrix A is\n    " \
    "left multiplies by a matrix T.\n    " \
    "The T matrix is\n    " \
    r".. math::""\n\n    " \
    r"    M = \begin{bmatrix}""\n    " \
    r"        1 - \frac{1}{N} & - \frac{1}{N} &  \dots & - \frac{1}{N} & - \frac{1}{N} \\""\n    " \
    r"        - \frac{1}{N} & 1 - \frac{1}{N} &  \dots & - \frac{1}{N} & - \frac{1}{N}  \\""\n    " \
    r"        \dots  & \dots  &  \dots & \dots & \dots   \\""\n    " \
    r"        - \frac{1}{N} & - \frac{1}{N} &  \dots & 1 - \frac{1}{N} & \dots  \\""\n    " \
    r"        - \frac{1}{N} & - \frac{1}{N} &  \dots & - \frac{1}{N} & - \frac{1}{N}  \\""\n    " \
    r"        \end{bmatrix}" \
    "\n\n    " \
    "In the context of the SEIK filter, this operation\n    " \
    "is partially the second term of Eq. (23) in [1]_\n    " \
    "and the T matrix is in Eq. (15)" \
    "\n\n    " \
    "References\n    " \
    "----------\n    " \
    ".. [1] Nerger, L., Janjić, T., Schröter, J., Hiller, W. (2012). \n    " \
    "       A unification of ensemble square root Kalman filters. \n    " \
    "       Monthly Weather Review, 140, 2335-2345. doi:10.1175/MWR-D-11-00102.1"

docstrings['etkf_Tleft'] = \
    "Remove column mean (ensemble mean).\n\n    " \
    "This function provides the ensemble anomaly of matrix A\n    " \
    "if it is an ensemble of state vectors.\n    " \
    "This function partially performs the second term of\n    " \
    "Eq. (34) with T defined as Eq. (31) in [1]_." \
    "\n\n    " \
    "References\n    " \
    "----------\n    " \
    ".. [1] Nerger, L., Janjić, T., Schröter, J., Hiller, W. (2012). \n    " \
    "       A unification of ensemble square root Kalman filters. \n    " \
    "       Monthly Weather Review, 140, 2335-2345. doi:10.1175/MWR-D-11-00102.1"

docstrings['estkf_OmegaA'] = \
    "Get left Householder transformation of A.\n\n    "\
    "This function partially performs the second term of Eq. (29)\n    " \
    "and the Householder matrix Omega is given in Eq. (24) in [1]_." \
    "\n\n    " \
    "References\n    " \
    "----------\n    " \
    ".. [1] Nerger, L., Janjić, T., Schröter, J., Hiller, W. (2012). \n    " \
    "       A unification of ensemble square root Kalman filters. \n    " \
    "       Monthly Weather Review, 140, 2335-2345. doi:10.1175/MWR-D-11-00102.1"

docstrings['enkf_omega'] = \
    "Generate a random matrix with orthogonal basis.\n\n    " \
    "This function generates the random matrix sampled\n    " \
    "from standard Gaussian distribution with different scaling options."

docstrings['seik_omega'] = \
    "Generate a random matrix with orthogonal basis.\n\n    " \
    "This function generates a uniform orthogonal matrix\n    " \
    "by iteratively applying Householder transformations.\n    " \
    "In this matrix, each column is orthogonal to the previous ones." \
    "\n    " \
    "This algorithm is documented in appendix of [1]_." \
    "\n\n    " \
    "References\n    " \
    "----------\n    " \
    ".. [1] Nerger, L., Janjić, T., Schröter, J., Hiller, W. (2012). \n    " \
    "       A unification of ensemble square root Kalman filters. \n    " \
    "       Monthly Weather Review, 140, 2335-2345. doi:10.1175/MWR-D-11-00102.1"

docstrings['incremental'] = \
    "Apply analysis increment to model state\n    " \
    "in model forecast phase.\n\n    " \
    "This function calls a user-supplied function\n    " \
    "to utilise the analysis increment stored by PDAF in the model.\n    " \
    "This may also be used for diagnostics purposes."

docstrings['add_increment'] = \
    "Add analysis increment stored by PDAF to given state vector."

docstrings['local_weights'] = \
    "Get a vector of localisation weights for given distances,\n    " \
    "cut-off radius, support radius, weighting type,\n    " \
    "and weighting function.\n\n    " \
    "This function is used in the analysis step of a filter\n    " \
    "to computes a localisation weight.\n\n    " \
    "Typically, in domain-localised filters, the function\n    " \
    "is called in user-supplied :func:`py__prodRinvA_l_pdaf`.\n    " \
    "In LEnKF, this function is called\n    " \
    "in user-supplied :func:`py__localize_covar_pdaf`.\n\n    " \
    "This function is usually only used without PDAF-OMI.\n\n    " \
    "This function is a vectorised version of\n    " \
    ":func:`pyPDAF.PDAF.local_weight` without any regulations."

docstrings['force_analysis'] = \
    "Perform assimilation after this function call.\n\n    " \
    "This function overwrite member index of the ensemble state\n    " \
    "by local_dim_ens (number of ensembles for current process,\n    " \
    "in full parallel setup, this is 1.) and the counter\n    " \
    "cnt_steps by nsteps-1.\n    " \
    "This forces that the analysis step is executed at\n    " \
    "the next call to PDAF assimilation functions."

docstrings['gather_obs_f2_flex'] = \
    "Gather full observation coordinates from processor\n    " \
    "local observation coordinates without PDAF-internal info.\n\n    " \
    "In the local filters (LESKTF, LETKF, LSEIK, LNETF)\n    " \
    "this function returns the full observation coordinates\n    " \
    "from process-local observation coordinates.\n\n    " \
    "This function has a similar functionality as\n    " \
    ":func:`pyPDAF.PDAF.gather_obs_f2`, but it does not depend\n    " \
    "on PDAF-internal observation dimension information,\n    " \
    "which is specified once :func:`pyPDAF.PDAF.gather_dim_obs_f`\n    " \
    "is executed.\n\n    " \
    "This function can also be used as a generic function\n    " \
    "to gather any 2D arrays\n    " \
    "where the second dimension should be concatenated."

docstrings['gather_obs_f_flex'] = \
    "Gather full observation from processor\n    " \
    "local observation without PDAF-internal info.\n\n    " \
    "In the local filters (LESKTF, LETKF, LSEIK, LNETF)\n    " \
    "this function returns the full observation\n    " \
    "from process-local observation.\n\n    " \
    "This function has a similar functionality as\n    " \
    ":func:`pyPDAF.PDAF.gather_obs_f`, but it does not depend\n    " \
    "on PDAF-internal observation dimension information,\n    " \
    "which is specified once :func:`pyPDAF.PDAF.gather_dim_obs_f`\n    " \
    "is executed.\n\n    " \
    "This function can also be used as a generic function\n    " \
    "to gather any 2D arrays\n    " \
    "where the second dimension should be concatenated."


docstrings['prepost'] = \
    "Perform pre-/post-processing.\n\n    " \
    "This is designed similar to a DA method subroutine\n    " \
    "where the ensemble/state vector collection, processing,\n    " \
    "and distribution are all depending on user-supplied functions." \
    "\n\n    " \
    "Compared to `pyPDAF.PDAF.assimilate_prepost`,\n    " \
    "this function does not set assimilation flag.\n\n    " \
    "The function is a combination of\n    " \
    ":func:`pyPDAF.PDAF.put_state_prepost`\n    " \
    "and :func:`pyPDAF.PDAF.get_state`.\n\n    " \
    "The user-supplied function is executed as follows:\n    " \
    "    1. py__collect_state_pdaf\n    " \
    "    2. py__prepoststep_state_pdaf\n    " \
    "    3. py__prepoststep_state_pdaf\n    " \
    "    4. py__distribute_state_pdaf\n    " \
    "    5. py__next_observation_pdaf"

docstrings['set_memberid'] = \
    "Set the ensemble member index to given value."

docstrings['set_comm_pdaf'] = \
    "Set the MPI communicator used by PDAF.\n\n    " \
    "By default, PDAF assumes it can use all available\n    " \
    "processes, i.e., `MPI_COMM_WORLD`.\n    " \
    "By using this function, we limit the number of processes\n    " \
    "that can be used by PDAF to given MPI communicator."

docstrings['set_offline_mode'] = \
    "Activate offline mode of PDAF."

docstrings['print_domain_stats'] = \
    "Print screen output of statistics of the local domains\n    " \
    "on current process.\n\n    " \
    "The statistics include the minimum, maximum, and\n    " \
    "average number of local domains per process."


docstrings['init_local_obsstats'] = \
    "Initialise the observation statistics of local domain.\n\n    " \
    "This function initialise the debug statistics used in\n    " \
    ":func:`pyPDAF.PDAF.incr_local_obsstats` and\n    " \
    ":func:`pyPDAF.PDAF.print_local_obsstats`.\n\n    " \
    "The statistics include:\n    " \
    "    - number of local domains with observations\n    " \
    "    - number of local domains without observationss\n    " \
    "    - maximum local observation dimension\n    " \
    "    - total observation dimension/total number of domains\n    " \
    "    - total observation dimension/number of domains with observations"


docstrings['incr_local_obsstats'] = \
    "Update observation statistics of local domain.\n\n    " \
    "To use this function, one should first initialise\n    " \
    "the statistics using :func:`pyPDAF.PDAF.init_local_obsstats`" \
    "\n\n    " \
    "The statistics include:\n    " \
    "    - number of local domains with observations\n    " \
    "    - number of local domains without observationss\n    " \
    "    - maximum local observation dimension\n    " \
    "    - total observation dimension/total number of domains\n    " \
    "    - total observation dimension/number of domains with observations"

docstrings['print_local_obsstats'] = \
    "Print screen output of the observation statistics of\n    " \
    "local domain.\n\n    " \
    "The statistics should be first initialised\n    " \
    "by :func:`pyPDAF.PDAF.init_local_obsstats`\n    " \
    "and can then be collected by\n    " \
    ":func:`pyPDAF.PDAF.incr_local_obsstats`.\n\n    " \
    "The statistics include:\n    " \
    "    - number of local domains with observations\n    " \
    "    - number of local domains without observationss\n    " \
    "    - maximum local observation dimension\n    " \
    "    - total observation dimension/total number of domains\n    " \
    "    - total observation dimension/number of domains with observations"

docstrings['omit_obs_omi'] = \
    "Omit observations with large ensemble mean innovation.\n\n    " \
    "This function first compute the ensemble mean,\n    "\
    "then set large observation error for observations\n    " \
    "with large ensemble mean innovation.\n    " \
    "This is used in the OMI functionality by\n    " \
    "some global filters, e.g. EnKF, LEnKF, PF, NETF.\n    " \
    "Therefore, one must first set the related options in OMI.\n    " \
    "See `pyPDAF.PDAF.omi_set_xxx` functions and\n    " \
    ":func:`pyPDAF.PDAF.omi_gather_obs`."


docstrings['omi_init'] = \
    "Allocating an array of `obs_f` derived types instances.\n\n    " \
    "This function initialises the number of observation types,\n    " \
    "which should be called at the start of the DA system\n    " \
    "after :func:`pyPDAF.PDAF.init`."

docstrings['omi_init_local'] = \
    "Allocating an array of `obs_l` derived types instances.\n\n    " \
    "This function initialises the number of observation types\n    " \
    "for each local analysis domain,\n    " \
    "which should be called at the start of the local analysis loop\n    " \
    "in :func:`py__init_dim_obs_l_pdaf`."

docstrings['omi_set_doassim'] = \
    "Setting the `doassim` attribute of `obs_f`\n    " \
    "for `i`-th observation type. This property must be\n    " \
    "explicitly set for OMI functionality.\n\n    " \
    "Properties of `obs_f` are typically set in user-supplied function\n    " \
    "`py__init_dim_obs_pdaf`.\n\n    " \
    "This is by default set to 0, which means that\n    " \
    "the given type of observation is not assimilated in the DA system."

docstrings['omi_set_disttype'] = \
    "Setting the observation localisation distance\n    " \
    "calculation method\n    " \
    "for `i`-th observation type. This is a mandatory property\n    " \
    "for OMI functionality.\n\n    " \
    "Properties of `obs_f` are typically set in user-supplied function\n    " \
    "`py__init_dim_obs_pdaf`.\n\n    " \
    "`disttype` determines the way the distance\n    " \
    "between observation and model grid is calculated in OMI.\n    " \
    "To perform distance computation, the observation coordinates" \
    "should be given by `ocoord_p` argument\n    " \
    "when :func:`pyPDAF.PDAF.omi_gather_obs` is called." \
    "\n\n    " \
    "See also `PDAF distance computation " \
    "<https://pdaf.awi.de/trac/wiki/OMI_observation_modules#thisobsdisttype>`_."

docstrings['omi_set_ncoord'] = \
    "Setting the number of spatial dimensions of observations\n    " \
    "for `i`-th observation type. This is a mandatory property\n    " \
    "for OMI functionality.\n\n    " \
    "Properties of `obs_f` are typically set in user-supplied function\n    " \
    "`py__init_dim_obs_pdaf`.\n\n    " \
    "`ncoord` gives the coordinate dimension of the observation.\n    " \
    "This information is used by observation distance computation\n    " \
    "for localisation.\n    " \
    "For example, `ncoord=2` for 2D observation coordinates."

docstrings['omi_set_id_obs_p'] = \
    "Setting the `id_obs_p` attribute of `obs_f`\n    " \
    "for `i`-th observation type. This is a mandatory property\n    " \
    "for OMI functionality.\n\n    " \
    "The function is typically used in user-supplied\n    " \
    "function `py__init_dim_obs_pdaf`.\n\n    " \
    "Here, `id_obs_p(nrows, dim_obs_p)` is a 2D array of integers.\n    " \
    "The value of `nrows` depends on the observation operator\n    " \
    "used for an observation.\n\n    " \
    "Examples:\n\n    " \
    "- `nrows=1`: observations are located on model grid point.\n    "\
    "  In this case,\n    " \
    "  `id_obs_p` stores the index of the state vector\n    " \
    "  (starting from 1) corresponds to the observations,\n    " \
    "  e.g. `id_obs_p[0, j] = i` means that the location\n    " \
    "  and variable of the `i`-th element of the state vector\n    " \
    "  is the same as the `j`-th observation.\n\n    " \
    "- `nrows=4`: each observation corresponds to\n    " \
    "  4 indices of elements in the state vector.\n    "\
    "  In this case,\n    " \
    "  the location of these elements is used to perform bi-linear interpolation\n    "\
    "  from model grid to observation location.\n    " \
    "  For interpolation, this information is used in the\n    "\
    "  :func:`pyPDAF.PDAF.omi_obs_op_interp_lin` functions.\n    " \
    "  This information can also be used to\n    " \
    "  perform a state vector averaging operator as\n    " \
    "  observation operator in :func:`pyPDAF.PDAF.omi_obs_op_gridavg`" \
    "  When interpolation is needed,\n    "\
    "  the weighting of the interpolation is done\n    "\
    "  in the :func:`pyPDAF.PDAF.omi_get_interp_coeff_lin`,\n    " \
    "  :func:`pyPDAF.PDAF.omi_get_interp_coeff_lin1D`,\n    "\
    "  and :func:`pyPDAF.PDAF.omi_get_interp_coeff_tri` functions.\n    " \
    "  The details of interpolation setup can be found at\n    " \
    "  `PDAF wiki page " \
    "<https://pdaf.awi.de/trac/wiki/OMI_observation_operators" \
    "#Initializinginterpolationcoefficients>`_.\n"

docstrings['omi_set_icoeff_p'] = \
    "Setting the observation interpolation coefficient\n    " \
    "for `i`-th observation type. This property is optional\n    " \
    "unless interpolations needed in observation operators\n    " \
    "operator.\n\n    " \
    "The function is typically used in user-supplied\n    " \
    "function `py__init_dim_obs_pdaf`.\n\n    " \
    "`icoeff_p(nrows, dim_obs_p)` is a 2D array of real number\n    " \
    "used to interpolate state vector to point-wise observation grid.\n    " \
    "The `nrows` is the number of state vector used to interpolate\n    " \
    "to one observation location.\n\n    " \
    "A suite of functions are provided to obtain these coefficients,\n    " \
    "which depend on `obs_f` attribute of `id_obs_p` and\n    " \
    "observation coordinates.\n\n    " \
    "See also :func:`pyPDAF.PDAF.set_id_obs_p`:\n    " \
    "    - :func:`pyPDAF.PDAF.omi_get_interp_coeff_lin1D`\n    " \
    "      1D interpolation coefficient\n    " \
    "    - :func:`pyPDAF.PDAF.omi_get_interp_coeff_lin`\n    " \
    "      linear interpolation coefficient for 1, 2 and 3D rectangular grids\n    " \
    "    - :func:`pyPDAF.PDAF.omi_get_interp_coeff_tri`\n    " \
    "      2D linear interpolation for triangular grids\n\n    " \
    "See also `PDAF documentation for OMI interpolations " \
    "<https://pdaf.awi.de/trac/wiki/OMI_observation_operators" \
    "#Initializinginterpolationcoefficients>`_."

docstrings['omi_set_domainsize'] = \
    "Setting the domain periodicity\n    " \
    "attribute of `obs_f`\n    " \
    "for `i`-th observation type. This property is optional\n    " \
    "unless localisation is used.\n\n    " \
    "The function is typically used in user-supplied\n    " \
    "function `py__init_dim_obs_pdaf`.\n\n    " \
    "`domainsize(ncoord)` specifies the size of the domain\n    " \
    "in each spatial dimension.\n    " \
    "This information is used to compute the Cartesian disance\n    " \
    "with periodic boundary. That is `disttype = 1 or 11`\n    " \
    "Domain size must be positive.\n    " \
    "If the value of one dimension is `<=0`,\n    " \
    "no periodicity is assumed in that dimension. "

docstrings['omi_set_obs_err_type'] = \
    "Setting the type of observation error distribution\n    " \
    "for `i`-th observation type. This property is optional\n    " \
    "unless a laplacian observation error distribution is used.\n\n    " \
    "The function is typically used in user-supplied\n    " \
    "function `py__init_dim_obs_pdaf`."

docstrings['omi_set_use_global_obs'] = \
    "Switch for only assimilating process-local observations\n    " \
    "for `i`-th observation type.\n\n    " \
    "The function is typically used in user-supplied\n    " \
    "function `py__init_dim_obs_pdaf`.\n\n    " \
    "The filters can be performed in parallel\n    " \
    "based on the filtering communicator, `comm_filter`.\n    " \
    "This is typically the case for the domain-localised filters,\n    " \
    "e.g., LESTK, LETKF, LSEIK, LNETF.\n    " \
    "In this case, observation vectors are stored in\n    " \
    "process-local vectors, `obs_p`. Each local\n    " \
    "process (`obs_p`) only stores a section of the full\n    " \
    "observation vector. This typically corresponds to the\n    " \
    "local domain corresponding to the filtering process,\n    " \
    "based on model domain decomposition.\n\n    " \
    "By default, `use_global_obs=1`. This means that\n    " \
    "PDAF-OMI assimilates the entire observation vector.\n    " \
    "One can choose to only assimilate observations\n    " \
    "in local process by setting `use_global_obs=0`.\n    " \
    "This can save computational cost used for\n    " \
    "observation distance calculations.\n\n    " \
    "However, it needs additional preparations to make\n    " \
    "PDAF-OMI aware of the limiting coordinates\n    " \
    "of a process sub-domain using\n    " \
    ":func:`pyPDAF.PDAF.omi_set_domain_limits` or\n    " \
    ":func:`pyPDAF.PDAF.omi_set_domain_limits_unstruc`.\n\n\n    " \
    "See Also\n    " \
    "--------\n    " \
    "https://pdaf.awi.de/trac/wiki/OMI_use_global_obs"

docstrings['omi_set_inno_omit'] = \
    "Setting innovation threshold for removing observation\n    " \
    "outliers. By default, no observations are omitted.\n\n    " \
    "This function is typically used in user-supplied\n    " \
    "function :func:`py__init_dim_obs_pdaf`.\n\n    " \
    "The observation omission is only activated when it is > 0.0.\n    " \
    "PDAF will omit observations where their squared\n    " \
    "the innovation of the ensemble mean is larger than\n    " \
    "the product of `inno_omit` and observation error variance.\n\n    " \
    "The observations are omitted by setting a very large\n    " \
    "observation error variance, i.e., a very small\n    " \
    "inverse of the observation error variance,  `inno_omit_ivar`.\n    " \
    "This can be set by :func:`pyPDAF.PDAF.omi_set_inno_omit_ivar`."

docstrings['omi_set_inno_omit_ivar'] = \
    "Setting the inverse of observation error variance for\n    " \
    "omitted observations.\n\n    " \
    "This should be set to a very small value relative to\n    " \
    "assimilated observations. By default, it is set to `1e-12`.\n\n    " \
    "This function is typically used in user-supplied function\n    " \
    ":func:`py__init_dim_obs_pdaf`."

docstrings['omi_gather_obs'] = \
    "Gather the dimension of a given type of observation across\n    " \
    "multiple local domains/filter processors.\n\n    " \
    "This function can be used in the user-supplied function of" \
    "\n    " \
    ":func:`py__init_dim_obs_f_pdaf`.\n\n    " \
    "This function does three things:\n    " \
    "    1. Receiving observation dimension on each local process." \
    "\n    " \
    "    2. Gather the total dimension of given observation type\n    " \
    "       across local process and the displacement of PE-local" \
    "\n    " \
    "       observations relative to the total observation vector" \
    "\n    " \
    "    3. Set the observation vector, observation coordinates, " \
    "\n    " \
    "       the inverse of the observation variance, and localisation" \
    "\n    " \
    "       radius for this observation type.\n\n    " \
    "\n\n    " \

docstrings['omi_gather_obsstate'] = "This function is used to implement custom observation operators. " \
                                    "See https://pdaf.awi.de/trac/wiki/OMI_observation_operators#Implementingyourownobservationoperator"
docstrings['omi_set_domain_limits'] = "This is used to set the domain limits for the use of `pyPDAF.PDAF.omi_set_use_global_obs`." \
                                      "Currently, it only supports 2D limitations. See https://pdaf.awi.de/trac/wiki/PDAFomi_additional_functionality#PDAFomi_set_domain_limit\n    "
docstrings['omi_set_debug_flag'] = "This sets the debug flag for OMI. If set to 1, debug information is printed to the screen.\n    " \
                                   "The debug flag can be set to 0 to stop the debugging. See https://pdaf.awi.de/trac/wiki/OMI_debugging"
docstrings['omi_deallocate_obs'] = \
    "Deallocate OMI-internal obsrevation arrays\n\n    " \
    "This function should not be called by users\n    " \
    "because it is called internally in PDAF."

docstrings['omi_obs_op_gridpoint'] = \
    "A (partial) identity observation operator\n\n    " \
    "This observation operator is used\n    " \
    "when observations and model use the same grid. \n\n    " \
    "The observations operator selects state vectors\n    " \
    "where observations are present based on properties given\n    " \
    "in `obs_f`, e.g., `id_obs_p`.\n\n    " \
    "The function is used in\n    " \
    "the user-supplied function :func:`py__obs_op_pdaf`."

docstrings['omi_obs_op_gridavg'] = "Observation operator that average values on given model grid points.\n\n    " \
                                   "The averaged model grid points are specified in `id_obs_p` property of `obs_f`,\n    " \
                                   "which can be set in :func:`pyPDAF.PDAF.omi_set_id_obs_p`.\n\n    "  \
                                   "The function is used in the user-supplied function `py__obs_op_pdaf`. "
docstrings['omi_obs_op_interp_lin'] = "Observation operator that linearly interpolates model grid values to observation location.\n\n    " \
                                      "The grid points used by linear interpolation is specified in `id_obs_p` of `obs_f`,\n    " \
                                      "which can be set by :func:`pyPDAF.PDAF.omi_set_id_obs_p`.\n\n    " \
                                      "The function also requires `icoeff_p` attribute of `obs_f`,\n    " \
                                      "which can be set by :func:`pyPDAF.PDAF.omi_set_icoeff_p`\n\n    " \
                                      "The interpolation coefficient can be obtained by " \
                                      ":func:`pyPDAF.PDAF.omi_get_interp_coeff_lin1D`,\n    " \
                                      ":func:`pyPDAF.PDAF.omi_get_interp_coeff_lin`, and\n    " \
                                      ":func:`pyPDAF.PDAF.omi_get_interp_coeff_tri`\n\n    " \
                                      "The details of interpolation setup can be found at\n    `PDAF wiki page " \
                                      "<https://pdaf.awi.de/trac/wiki/OMI_observation_operators#Initializinginterpolationcoefficients>`_\n\n    " \
                                      "The function is used in the user-supplied function `py__obs_op_pdaf`. "
docstrings['omi_obs_op_adj_gridavg'] = "The adjoint observation operator of :func:`pyPDAF.PDAF.omi_obs_op_gridavg`."
docstrings['omi_obs_op_adj_gridpoint'] = "The adjoint observation operator of :func:`pyPDAF.PDAF.omi_obs_op_gridpoint`."
docstrings['omi_obs_op_adj_interp_lin'] = "The adjoint observation operator of :func:`pyPDAF.PDAF.omi_obs_op_interp_lin`."
docstrings['omi_get_interp_coeff_tri'] = "The coefficient for linear interpolation in 2D on unstructure triangular grid.\n\n    " \
                                         "The resulting coefficient is used in :func:`omi_obs_op_interp_lin`.\n\n    " \
                                         "This function is for triangular model grid interpolation coefficients " \
                                         "determined as barycentric coordinates."
docstrings['omi_get_interp_coeff_lin1D'] = "The coefficient for linear interpolation in 1D.\n\n    " \
                                           "The resulting coefficient is used in :func:`omi_obs_op_interp_lin`.\n\n    "
docstrings['omi_get_interp_coeff_lin'] = "The coefficient for linear interpolation up to 3D.\n\n    " \
                                         "The resulting coefficient is used in :func:`omi_obs_op_interp_lin`.\n\n    " \
                                         "See introduction in `PDAF-OMI wiki page \n    " \
                                         "<https://pdaf.awi.de/trac/wiki/OMI_observation_operators#PDAFomi_get_interp_coeff_lin>`_"


docstrings['omi_init_obs_f_cb'] = "This function is an internal PDAF-OMI function that is used as a call-back function to initialise the observation vector. " \
                                  "This could be used to modify the observation vector when OMI is used with `pyPDAF.PDAF.assimilate_xxx` instead of `pyPDAF.PDAF.omi_assimilate_xxx`."
docstrings['omi_init_obsvar_cb'] = "This function is an internal PDAF function that is used as a call-back function to initialise the observation error variance. " \
                                   "This could be used to modify the observation variance when OMI is used with `pyPDAF.PDAF.assimilate_xxx` instead of `pyPDAF.PDAF.omi_assimilate_xxx`."
docstrings['omi_g2l_obs_cb'] = "This function is an internal PDAF-OMI function that is used as a call-back function to convert between global and local observation vectors in domain localisation.\n    "
docstrings['omi_init_obs_l_cb'] = "This function is an internal PDAF-OMI function that is used as a call-back function to initialise local observation vector in domain localisation. " \
                                  "This could be used to modify the observation variance when OMI is used with `pyPDAF.PDAF.assimilate_xxx` instead of `pyPDAF.PDAF.omi_assimilate_xxx`."
docstrings['omi_init_obsvar_l_cb'] = "This function is an internal PDAF-OMI function that is used as a call-back function to initialise local observation vector in domain localisation. " \
                                     "This could be used to modify the observation variance when OMI is used with `pyPDAF.PDAF.assimilate_xxx` instead of `pyPDAF.PDAF.omi_assimilate_xxx`."
docstrings['omi_prodRinvA_l_cb'] = "This function is an internal PDAF-OMI function that is used as a call-back function to perform the matrix multiplication inverse of local observation error covariance and a matrix A in domain localisation. " \
                                   "This could be used to modify the observation variance when OMI is used with `pyPDAF.PDAF.assimilate_xxx` instead of `pyPDAF.PDAF.omi_assimilate_xxx`."
docstrings['omi_likelihood_l_cb'] = "This is an internal PDAF-OMI function that is used as a call-back function to compute the likelihood of the observation for a given ensemble member according to the observations used for the local analysis in the localized LNETF. " \
    "This could be used to modify the observation variance when OMI is used with `pyPDAF.PDAF.assimilate_xxx` instead of `pyPDAF.PDAF.omi_assimilate_xxx`. See https://pdaf.awi.de/trac/wiki/U_likelihood_l"
docstrings['omi_prodRinvA_cb'] = "This function is an internal PDAF-OMI function that is used as a call-back function to perform the matrix multiplication inverse of observation errro covariance and a matrix A. " \
                                 "This could be used to modify the observation variance when OMI is used with `pyPDAF.PDAF.assimilate_xxx` instead of `pyPDAF.PDAF.omi_assimilate_xxx`."
docstrings['omi_likelihood_cb'] = "This is an internal PDAF-OMI function that is used as a call-back function to compute the likelihood of the observation for a given ensemble member according to the observations used for the local analysis for NETF or particle filter. " \
    "This could be used to modify the observation variance when OMI is used with `pyPDAF.PDAF.assimilate_xxx` instead of `pyPDAF.PDAF.omi_assimilate_xxx`. See https://pdaf.awi.de/trac/wiki/U_likelihood_l"
docstrings['omi_add_obs_error_cb'] = "This is an internal PDAF-OMI function that is used as a call-back function to add random observation error to stochastic EnKF. " \
                                     "This could be used to modify the observation variance when OMI is used with `pyPDAF.PDAF.assimilate_xxx` instead of `pyPDAF.PDAF.omi_assimilate_xxx`. See https://pdaf.awi.de/trac/wiki/U_likelihood_l"
docstrings['omi_init_obscovar_cb'] = "This is an internal PDAF-OMI function that is used as a call-back function to construct a full observation error covariance matrix used only in stochastic EnKF. " \
                                     "This could be used to modify the observation variance when OMI is used with `pyPDAF.PDAF.assimilate_xxx` instead of `pyPDAF.PDAF.omi_assimilate_xxx`."
docstrings['omi_init_obserr_f_cb'] = "This is an internal PDAF-OMI function that is used as a call-back function to construct a full observation error covariance matrix used only in stochastic EnKF. " \
                                     "This could be used to modify the observation variance when OMI is used with `pyPDAF.PDAF.assimilate_xxx` instead of `pyPDAF.PDAF.omi_assimilate_xxx`."
docstrings['omi_prodRinvA_hyb_l_cb'] = "This function is an internal PDAF-OMI function that is used as a call-back function to perform the matrix multiplication inverse of local observation error covariance and a matrix A in LKNETF. " \
                                       "This could be used to modify the observation variance when OMI is used with `pyPDAF.PDAF.assimilate_xxx` instead of `pyPDAF.PDAF.omi_assimilate_xxx`."
docstrings['omi_likelihood_hyb_l_cb'] = "This is an internal PDAF-OMI function that is used as a call-back function to compute the likelihood of the observation for a given ensemble member according to the observations used for the local analysis in LKNETF. " \
                                        "This could be used to modify the observation variance when OMI is used with `pyPDAF.PDAF.assimilate_xxx` instead of `pyPDAF.PDAF.omi_assimilate_xxx`. See https://pdaf.awi.de/trac/wiki/U_likelihood_l"

docstrings['omi_obsstats_l'] = "This function is called in the update routine of local filters and write statistics on locally used and excluded observations."
docstrings['omi_weights_l'] = "This function computes a weight vector according to the distances of observations from the local analysis domain with a vector of localisation radius."
docstrings['omi_weights_l_sgnl'] = "This function computes a weight vector according to the distances of observations from the local analysis domain with given localisation radius."
docstrings['omi_check_error'] = "This function returns the value of the PDAF-OMI internal error flag."
docstrings['omi_gather_obsdims'] = "This function gathers the information about the full dimension of each observation type in each process-local subdomain."
docstrings['omi_obsstats'] = "The function is called in the update routine of global filters and writes statistics on used and excluded observations."
docstrings['omi_init_dim_obs_l_iso'] = "The function has to be called in `init_dim_obs_l_OBTYPE` in each observation module if a domain-localized filter (LESTKF/LETKF/LNETF/LSEIK)is used. " \
                                       "It initialises the local observation information for PDAF-OMI for a single local analysis domain. This is used for isotropic localisation " \
                                       "where the localisation radius is the same in all directions."
docstrings['omi_init_dim_obs_l_noniso'] = "The function has to be called in `init_dim_obs_l_OBTYPE` in each observation module if a domain-localized filter (LESTKF/LETKF/LNETF/LSEIK)is used. " \
                                          "It initialises the local observation information for PDAF-OMI for a single local analysis domain. This is used for non-isotropic localisation " \
                                          "where the localisation radius is different in each direction. See https://pdaf.awi.de/trac/wiki/OMI_observation_modules#init_dim_obs_l_OBSTYPE and https://pdaf.awi.de/trac/wiki/PDAFomi_init_dim_obs_l#Settingsfornon-isotropiclocalization."
docstrings['omi_init_dim_obs_l_noniso_locweights'] = "The function has to be called in `init_dim_obs_l_OBTYPE` in each observation module if a domain-localized filter (LESTKF/LETKF/LNETF/LSEIK)is used. " \
    "It initialises the local observation information for PDAF-OMI for a single local analysis domain. This is used for non-isotropic localisation and different weight functions for horizontal and vertical directions. " \
    "See https://pdaf.awi.de/trac/wiki/OMI_observation_modules#init_dim_obs_l_OBSTYPE and https://pdaf.awi.de/trac/wiki/PDAFomi_init_dim_obs_l#Settingdifferentweightfunctsforhorizontalandverticaldirections."
docstrings['omi_localize_covar_iso'] = "The function has to be called in `localize_covar_OBTYPE` in each observation module. It applies the covariance localisation in stochastic EnKF. This is used for isotropic localisation " \
                                       "where the localisation radius is the same in all directions. See https://pdaf.awi.de/trac/wiki/PDAFomi_localize_covar"
docstrings['omi_localize_covar_noniso'] = "The function has to be called in `localize_covar_OBTYPE` in each observation module. It applies the covariance localisation in stochastic EnKF. This is used for non-isotropic localisation " \
    "where the localisation radius is different. See https://pdaf.awi.de/trac/wiki/PDAFomi_localize_covar"
docstrings['omi_localize_covar_noniso_locweights'] = "The function has to be called in `localize_covar_OBTYPE` in each observation module. It applies the covariance localisation in stochastic EnKF. This is used for non-isotropic localisation with different weight function for horizontal and vertical directions. " \
    "where the localisation radius is different. See https://pdaf.awi.de/trac/wiki/PDAFomi_localize_covar"

docstrings['omi_omit_by_inno_l_cb'] = "The function is called during the analysis step on each local analysis domain. " \
                                      "It checks the size of the innovation and sets the observation error to a high value " \
                                      "if the squared innovation exceeds a limit relative to the observation error variance." \
                                      "This function is an internal PDAF-OMI function that is used as a call-back function. " \
                                      "This could be used to modify the observation vector when OMI is used with `pyPDAF.PDAF.assimilate_xxx` instead of `pyPDAF.PDAF.omi_assimilate_xxx`."

docstrings['omi_omit_by_inno_cb'] = "The function is called during the analysis step of a global filter. " \
                                    "It checks the size of the innovation and " \
                                    "sets the observation error to a high value " \
                                    "if the squared innovation exceeds a limit relative to the observation error variance.""This function is called in the update routine of local filters and write statistics on locally used and excluded observations." \
                                    "This function is an internal PDAF-OMI function that is used as a call-back function. " \
                                    "This could be used to modify the observation vector when OMI is used with `pyPDAF.PDAF.assimilate_xxx` instead of `pyPDAF.PDAF.omi_assimilate_xxx`."

docstrings['omi_set_localization'] = "This function sets localization information " \
                                     "(locweight, cradius, sradius) in OMI, " \
                                     "and allocates local arrays for cradius and sradius, i.e. `obs_l`. " \
                                     "This variant is for isotropic localization. " \
                                     "The function is used by user-supplied implementations of " \
                                     "`pyPDAF.PDAF.omi_init_dim_obs_l_iso`. "
docstrings['omi_set_localization_noniso'] = "This function sets localization information " \
                                            "(locweight, cradius, sradius) in OMI, " \
                                            "and allocates local arrays for cradius and sradius, i.e. `obs_l`. " \
                                            "This variant is for non-isotropic localization. " \
                                            "The function is used by user-supplied implementations of " \
                                            "`pyPDAF.PDAF.omi_init_dim_obs_l_noniso`. "
docstrings['omi_set_dim_obs_l'] = "This function initialises number local observations. " \
                                  "It also returns number of local observations up to the current observation type. " \
                                  "It is used by a user-supplied implementations of " \
                                  "`pyPDAF.PDAF.omi_init_dim_obs_l_xxx`."
docstrings['omi_store_obs_l_index'] = "This function stores the mapping index " \
                                      "between the global and local observation vectors, " \
                                      "the distance and the cradius and sradius " \
                                      "for a single observations in OMI. " \
                                      "This variant is for non-factorised localisation. " \
                                      "The function is used by user-supplied implementations of " \
                                      "`pyPDAF.PDAF.omi_init_dim_obs_l_iso` or `pyPDAF.PDAF.omi_init_dim_obs_l_noniso`. "
docstrings['omi_store_obs_l_index_vdist'] = "This function stores the mapping index " \
                                            "between the global and local observation vectors, " \
                                            "the distance and the cradius and sradius " \
                                            "for a single observations in OMI. " \
                                            "This variant is for 2D+1D factorised localisation.\n    " \
                                            "The function is used by user-supplied implementations of " \
                                            "`pyPDAF.PDAF.omi_init_dim_obs_l_noniso_locweights`."


docstrings['local_set_indices'] = "Set index vector to map local state vector to global state vectors. " \
                                  "This is called in the user-supplied function `py__init_dim_l_pdaf`."
docstrings['local_set_increment_weights'] = "This function initialises a PDAF_internal local array " \
                                            "of increment weights. The weights are applied in " \
                                            "in PDAF_local_l2g_cb where the local state vector\n    " \
                                            "is weighted by given weights. " \
                                            "These can e.g. be used to apply a vertical localisation."
docstrings['local_clear_increment_weights'] = "This function deallocates the local increment weight vector " \
                                              "in `pyPDAF.PDAF.local_set_increment_weights` if it is allocated"
docstrings['local_g2l_cb'] = "Project a global to a local state vector for the localized filters.\n    " \
                             "This is the full callback function to be used internally. The mapping " \
                             "is done using the index vector id_lstate_in_pstate that is initialised " \
                             "in `pyPDAF.PDAF.local_set_indices`."
docstrings['local_l2g_cb'] = "Initialise elements of a global state vector from a local state vector.\n    " \
                             "This is the full callback function to be used internally. The mapping " \
                             "is done using the index vector `id_lstate_in_pstate` that is initialised " \
                             "in `pyPDAF.PDAF.local_set_indices`. \n    \n    " \
                             "To exclude any element of the local state vector from the initialisation" \
                             "one can set the corresponding index value to 0."
