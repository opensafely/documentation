---
search:
  exclude: true
---
---8<-- 'includes/cohort-extractor-deprecated.md'

This section describes each available function for creating variables within a study definition.

For more information on the datasets contained within the OpenSAFELY database, see the [Data sources section](../data-sources/intro.md).

For more information on writing a study definition, go to the [study definition section](study-def.md).


## Primary Care Record

These variables are derived from data held in the patients' primary care records.
&nbsp;

<div class="doc doc-object doc-function">


<h4 id="cohortextractor.patients.registered_as_of" class="doc doc-heading">
            <code class="highlight language-python"><span class="n">registered_as_of</span><span class="p">(</span><span class="n">reference_date</span><span class="p">,</span> <span class="n">return_expectations</span><span class="o">=</span><span class="kc">None</span><span class="p">)</span></code>

<a href="#cohortextractor.patients.registered_as_of" class="headerlink" title="Permanent link">🔗</a></h4>


    <div class="doc doc-contents first">

        <p>All patients registered on the given date. Note this function passes arguments
to registered_with_one_practice_between()</p>


<p><span class="doc-section-title">Parameters:</span></p>
    <table>
      <thead>
        <tr>
          <th>Name</th>
          <th>Type</th>
          <th>Description</th>
          <th>Default</th>
        </tr>
      </thead>
      <tbody>
          <tr class="doc-section-item">
            <td>
                <code>reference_date</code>
            </td>
            <td>
            </td>
            <td>
              <div class="doc-md-description">
                <p>date of interest as a string with the format <code>YYYY-MM-DD</code>. Filters results to
patients registered at a practice on the given date.</p>
              </div>
            </td>
            <td>
                <em>required</em>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>return_expectations</code>
            </td>
            <td>
            </td>
            <td>
              <div class="doc-md-description">
                <p>a dictionary containing an expectation definition defining an <code>incidence</code>
between <code>0</code> and <code>1</code>.</p>
              </div>
            </td>
            <td>
                  <code>None</code>
            </td>
          </tr>
      </tbody>
    </table>


    <p><span class="doc-section-title">Returns:</span></p>
    <table>
      <thead>
        <tr>
<th>Name</th>          <th>Type</th>
          <th>Description</th>
        </tr>
      </thead>
      <tbody>
          <tr class="doc-section-item">
<td><code>list</code></td>            <td>
            </td>
            <td>
              <div class="doc-md-description">
                <p>of integers of <code>1</code> or <code>0</code>.</p>
              </div>
            </td>
          </tr>
      </tbody>
    </table>
        <p>Example:</p>
<div class="highlight"><pre><span></span><code>This creates a variable &quot;registered&quot; with patient returning an integer of `1` if patient registered
at date. Patients who are not registered return an integer of `0`:

    registered=patients.registered_as_of(
        &quot;2020-03-01&quot;,
        return_expectations={&quot;incidence&quot;: 0.98}
    )
</code></pre></div>


    </div>

</div><p>&nbsp;</p>


<div class="doc doc-object doc-function">


<h4 id="cohortextractor.patients.registered_with_one_practice_between" class="doc doc-heading">
            <code class="highlight language-python"><span class="n">registered_with_one_practice_between</span><span class="p">(</span><span class="n">start_date</span><span class="p">,</span> <span class="n">end_date</span><span class="p">,</span> <span class="n">return_expectations</span><span class="o">=</span><span class="kc">None</span><span class="p">)</span></code>

<a href="#cohortextractor.patients.registered_with_one_practice_between" class="headerlink" title="Permanent link">🔗</a></h4>


    <div class="doc doc-contents first">

        <p>All patients registered with the same practice through the given period.</p>
<p>Note, this function does not return all patients registered with the same practice through
the given time period when this practice changes its <abbr title="Electronic Health Record">EHR</abbr> provider. ß
To capture this information, please use <code>with_complete_gp_consultation_history_between()</code></p>


<p><span class="doc-section-title">Parameters:</span></p>
    <table>
      <thead>
        <tr>
          <th>Name</th>
          <th>Type</th>
          <th>Description</th>
          <th>Default</th>
        </tr>
      </thead>
      <tbody>
          <tr class="doc-section-item">
            <td>
                <code>start_date</code>
            </td>
            <td>
            </td>
            <td>
              <div class="doc-md-description">
                <p>start date of interest of period as a string with the format <code>YYYY-MM-DD</code>.
Together with end date, this filters results to patients registered at a practice between two dates</p>
              </div>
            </td>
            <td>
                <em>required</em>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>end_date</code>
            </td>
            <td>
            </td>
            <td>
              <div class="doc-md-description">
                <p>end date of interest of period as a string with the format <code>YYYY-MM-DD</code>.
Together with start date, this filters results to patients registered at a practice between two dates</p>
              </div>
            </td>
            <td>
                <em>required</em>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>return_expectations</code>
            </td>
            <td>
            </td>
            <td>
              <div class="doc-md-description">
                <p>a dictionary containing an expectation definition defining an <code>incidence</code>
between <code>0</code> and <code>1</code>.</p>
              </div>
            </td>
            <td>
                  <code>None</code>
            </td>
          </tr>
      </tbody>
    </table>


    <p><span class="doc-section-title">Returns:</span></p>
    <table>
      <thead>
        <tr>
<th>Name</th>          <th>Type</th>
          <th>Description</th>
        </tr>
      </thead>
      <tbody>
          <tr class="doc-section-item">
<td><code>list</code></td>            <td>
            </td>
            <td>
              <div class="doc-md-description">
                <p>of integers of <code>1</code> or <code>0</code>.</p>
              </div>
            </td>
          </tr>
      </tbody>
    </table>
        <p>Example:</p>
<div class="highlight"><pre><span></span><code>This creates a variable `registered_one` with patient returning an integer of `1` if patient registered
at one practice between two dates. Patients who are not registered return an integer of `0`.

    registered_one=patients.registered_with_one_practice_between(
        start_date=&quot;2020-03-01&quot;,
        end_date=&quot;2020-06-01&quot;,
        return_expectations={&quot;incidence&quot;: 0.90}
    )
</code></pre></div>


    </div>

</div><p>&nbsp;</p>


<div class="doc doc-object doc-function">


<h4 id="cohortextractor.patients.date_deregistered_from_all_supported_practices" class="doc doc-heading">
            <code class="highlight language-python"><span class="n">date_deregistered_from_all_supported_practices</span><span class="p">(</span><span class="n">on_or_before</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span> <span class="n">on_or_after</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span> <span class="n">between</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span> <span class="n">date_format</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span> <span class="n">return_expectations</span><span class="o">=</span><span class="kc">None</span><span class="p">)</span></code>

<a href="#cohortextractor.patients.date_deregistered_from_all_supported_practices" class="headerlink" title="Permanent link">🔗</a></h4>


    <div class="doc doc-contents first">

        <p>Returns the date (if any) on which the patient de-registered from all
practices for which OpenSAFELY has data. Events which occur in primary care
after this date will not be recorded in the platform (though there may be
data from other sources e.g. <abbr title="Second Generation Surveillance System: an application that stores and manages data on laboratory isolates and notifications. PHE's preferred method for capturing routine laboratory surveillance data on infectious diseases and antimicrobial resistance from laboratories across England">SGSS</abbr>, <abbr title="Covid-19 Patient Notification System - the route by which NHS England are informed of COVID-19-positive, deaths in hospital">CPNS</abbr>).</p>


<p><span class="doc-section-title">Parameters:</span></p>
    <table>
      <thead>
        <tr>
          <th>Name</th>
          <th>Type</th>
          <th>Description</th>
          <th>Default</th>
        </tr>
      </thead>
      <tbody>
          <tr class="doc-section-item">
            <td>
                <code>on_or_before</code>
            </td>
            <td>
            </td>
            <td>
              <div class="doc-md-description">
                <p>date of interest as a string with the format <code>YYYY-MM-DD</code>. Filters results to
on or before the given date.</p>
              </div>
            </td>
            <td>
                  <code>None</code>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>on_or_after</code>
            </td>
            <td>
            </td>
            <td>
              <div class="doc-md-description">
                <p>date of interest as a string with the format <code>YYYY-MM-DD</code>. Filters results to
on or after the given date.</p>
              </div>
            </td>
            <td>
                  <code>None</code>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>between</code>
            </td>
            <td>
            </td>
            <td>
              <div class="doc-md-description">
                <p>two dates of interest as a list with each date as a string with the format <code>YYYY-MM-DD</code>.
Filters results to between the two dates provided (inclusive).
The two dates must be in chronological order.</p>
              </div>
            </td>
            <td>
                  <code>None</code>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>date_format</code>
            </td>
            <td>
            </td>
            <td>
              <div class="doc-md-description">
                <p>a string detailing the format of the dates to be returned. It can be <code>YYYY-MM-DD</code>,
<code>YYYY-MM</code> or <code>YYYY</code> and wherever possible the least disclosive data should be returned. i.e returning
only year is less disclosive than a date with day, month and year.</p>
              </div>
            </td>
            <td>
                  <code>None</code>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>return_expectations</code>
            </td>
            <td>
            </td>
            <td>
              <div class="doc-md-description">
                <p>a dictionary defining the incidence and distribution of expected value
within the population in question.</p>
              </div>
            </td>
            <td>
                  <code>None</code>
            </td>
          </tr>
      </tbody>
    </table>


    <p><span class="doc-section-title">Returns:</span></p>
    <table>
      <thead>
        <tr>
<th>Name</th>          <th>Type</th>
          <th>Description</th>
        </tr>
      </thead>
      <tbody>
          <tr class="doc-section-item">
<td><code>list</code></td>            <td>
            </td>
            <td>
              <div class="doc-md-description">
                <p>of strings with a date format returned if patient had deregistered, otherwise empty</p>
              </div>
            </td>
          </tr>
      </tbody>
    </table>
        <p>Example:</p>
<div class="highlight"><pre><span></span><code>A variable called `dereg_date` is created with returns a date of de-registration if patient has
deregistered from a practice within the dataset within the specified time period.

    dereg_date=patients.date_deregistered_from_all_supported_practices(
        on_or_after=&quot;2020-03-01&quot;,
        date_format=&quot;YYYY-MM-DD&quot;,
        return_expectations={
            {&quot;date&quot;: {&quot;earliest&quot;: &quot;2020-03-01&quot;},
            &quot;incidence&quot;: 0.05
        }
    )
</code></pre></div>


    </div>

</div><p>&nbsp;</p>


<div class="doc doc-object doc-function">


<h4 id="cohortextractor.patients.with_complete_gp_consultation_history_between" class="doc doc-heading">
            <code class="highlight language-python"><span class="n">with_complete_gp_consultation_history_between</span><span class="p">(</span><span class="n">start_date</span><span class="p">,</span> <span class="n">end_date</span><span class="p">,</span> <span class="n">return_expectations</span><span class="o">=</span><span class="kc">None</span><span class="p">)</span></code>

<a href="#cohortextractor.patients.with_complete_gp_consultation_history_between" class="headerlink" title="Permanent link">🔗</a></h4>


    <div class="doc doc-contents first">

        <p>All patients registered with the same practice through the given period, when the practice
used the same <abbr title="Electronic Health Record">EHR</abbr> system (for example, SystmOne) through the given period.</p>
<p>Further details:
The concept of a "consultation" in <abbr title="Electronic Health Record">EHR</abbr> systems does not map exactly
to the GP-patient interaction we're interested in (see <code>with_gp_consultations()</code>) so there is some
processing required on the part of the <abbr title="Electronic Health Record">EHR</abbr> vendor to produce the
consultation record we need. This does not happen automatically as part of
the GP2GP transfer, and therefore this query can be used to find just those
patients for which the full history is available. This means finding patients
who have been continuously registered with a single <abbr title="The company behind the SystmOne EHR">TPP</abbr>-using practice
throughout a time period.</p>


<p><span class="doc-section-title">Parameters:</span></p>
    <table>
      <thead>
        <tr>
          <th>Name</th>
          <th>Type</th>
          <th>Description</th>
          <th>Default</th>
        </tr>
      </thead>
      <tbody>
          <tr class="doc-section-item">
            <td>
                <code>start_date</code>
            </td>
            <td>
            </td>
            <td>
              <div class="doc-md-description">
                <p>start date of interest as a string with the format <code>YYYY-MM-DD</code></p>
              </div>
            </td>
            <td>
                <em>required</em>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>end_date</code>
            </td>
            <td>
            </td>
            <td>
              <div class="doc-md-description">
                <p>end date of interest as a string with the format <code>YYYY-MM-DD</code></p>
              </div>
            </td>
            <td>
                <em>required</em>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>return_expectations</code>
            </td>
            <td>
            </td>
            <td>
              <div class="doc-md-description">
                <p>a dictionary defining the incidence and distribution of expected value
within the population in question.</p>
              </div>
            </td>
            <td>
                  <code>None</code>
            </td>
          </tr>
      </tbody>
    </table>


    </div>

</div><p>&nbsp;</p>


<div class="doc doc-object doc-function">


<h4 id="cohortextractor.patients.registered_practice_as_of" class="doc doc-heading">
            <code class="highlight language-python"><span class="n">registered_practice_as_of</span><span class="p">(</span><span class="n">date</span><span class="p">,</span> <span class="n">returning</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span> <span class="n">return_expectations</span><span class="o">=</span><span class="kc">None</span><span class="p">)</span></code>

<a href="#cohortextractor.patients.registered_practice_as_of" class="headerlink" title="Permanent link">🔗</a></h4>


    <div class="doc doc-contents first">

        <p>Return patients' practice address characteristics such as STP or MSOA</p>


<p><span class="doc-section-title">Parameters:</span></p>
    <table>
      <thead>
        <tr>
          <th>Name</th>
          <th>Type</th>
          <th>Description</th>
          <th>Default</th>
        </tr>
      </thead>
      <tbody>
          <tr class="doc-section-item">
            <td>
                <code>date</code>
            </td>
            <td>
            </td>
            <td>
              <div class="doc-md-description">
                <p>date of interest as a string with the format <code>YYYY-MM-DD</code>. Filters results to the given date.</p>
              </div>
            </td>
            <td>
                <em>required</em>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>returning</code>
            </td>
            <td>
            </td>
            <td>
              <div class="doc-md-description">
                <p>string indicating value to be returned. Options are:</p>
<ul>
<li><code>msoa</code>: Middle Layer Super Output Area codes</li>
<li><code>nuts1_region_name</code>: 9 English regions</li>
<li><code>stp_code</code>: Sustainability Transformation Partnerships codes</li>
<li><code>pseudo_id</code>: Pseudonymised GP practice identifier</li>
<li><code>rct__{trial_name}__{property_name}</code>: Properties from a Cluster
   Randomised Controlled Trial (<a href="#cohortextractor.patients.registered_practice_as_of--cluster-rcts">see below</a>)</li>
</ul>
              </div>
            </td>
            <td>
                  <code>None</code>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>return_expectations</code>
            </td>
            <td>
            </td>
            <td>
              <div class="doc-md-description">
                <p>a dict defining the <code>rate</code> and the <code>categories</code> returned with ratios</p>
              </div>
            </td>
            <td>
                  <code>None</code>
            </td>
          </tr>
      </tbody>
    </table>


    <p><span class="doc-section-title">Returns:</span></p>
    <table>
      <thead>
        <tr>
<th>Name</th>          <th>Type</th>
          <th>Description</th>
        </tr>
      </thead>
      <tbody>
          <tr class="doc-section-item">
<td><code>list</code></td>            <td>
            </td>
            <td>
              <div class="doc-md-description">
                <p>of strings</p>
              </div>
            </td>
          </tr>
      </tbody>
    </table>


<p><span class="doc-section-title">Raises:</span></p>
    <table>
      <thead>
        <tr>
          <th>Type</th>
          <th>Description</th>
        </tr>
      </thead>
      <tbody>
          <tr class="doc-section-item">
            <td>
                  <code><span title="ValueError">ValueError</span></code>
            </td>
            <td>
              <div class="doc-md-description">
                <p>if unsupported <code>returning</code> argument is provided</p>
              </div>
            </td>
          </tr>
      </tbody>
    </table>
        <p>Example:</p>
<div class="highlight"><pre><span></span><code>This creates a variable called `region` based on practice address of the patient:

    region=patients.registered_practice_as_of(
        &quot;2020-02-01&quot;,
        returning=&quot;nuts1_region_name&quot;,
        return_expectations={
            &quot;rate&quot;: &quot;universal&quot;,
            &quot;category&quot;: {
                &quot;ratios&quot;: {
                    &quot;North East&quot;: 0.1,
                    &quot;North West&quot;: 0.1,
                    &quot;Yorkshire and the Humber&quot;: 0.1,
                    &quot;East Midlands&quot;: 0.1,
                    &quot;West Midlands&quot;: 0.1,
                    &quot;East of England&quot;: 0.1,
                    &quot;London&quot;: 0.2,
                    &quot;South East&quot;: 0.2,
                },
            },
        },
    )


##### Cluster RCTs

Support is currently available for randomised controlled trials clustered at
practice level (though we are also happy to add support for RCTs randomised
at person-level).

A series of data files supplied by the trialists will be imported into
OpenSAFELY; this will indicate which practices are enrolled, their assignment
to an intervention group, and any other relevant practice properties or data
gathered as part of the RCT outside of OpenSAFELY (e.g. number of GPs/nurses,
number of practice visits made).

These RCT variables are only available for use by the researchers officially
nominated by the responsible research group.

There is special syntax for accessing this data using the `returning` argument:

    rct__{trial_name}__{property_name}

(Note the double underscores separating `rct`, trial name and property name.)

For example, for a trial called `germdefence` which has a property called
`deprivation_pctile`, a variable can be created with:

    practice_deprivation_pctile=patients.registered_practice_as_of(
        &quot;2020-01-01&quot;,
        returning=&quot;rct__germdefence__deprivation_pctile&quot;,
        return_expectations={
            &quot;rate&quot;: &quot;universal&quot;,
            &quot;category&quot;: {
                &quot;ratios&quot;: {
                    &quot;1&quot;: 0.5,
                    &quot;2&quot;: 0.5
                },
            },
        },
    )

The special property `enrolled` is a boolean indicating whether the practice
was enrolled in the trial. It will be 1 for all intervention AND control practices
and 0 for any practices which are not part of the trial.

All other properties are returned as strings, exactly as supplied by the
trialists.  For the `germdefence` trial the available properties are:

    trial_arm
    av_rooms_per_house
    deprivation_pctile
    group_mean_behaviour_mean
    group_mean_intention_mean
    hand_behav_practice_mean
    hand_intent_practice_mean
    imd_decile
    intcon
    meanage
    medianage
    minority_ethnic_total
    n_completers_hw_behav
    n_completers_ri_behav
    n_completers_ri_intent
    n_engaged_pages_viewed_mean_mean
    n_engaged_visits_mean
    n_goalsetting_completers_per_practice
    n_pages_viewed_mean
    n_times_visited_mean
    n_visits_practice
    prop_engaged_visits
    total_visit_time_mean
</code></pre></div>
<p>The data resulting from the <abbr title="specifies the patients you want to include in your study and defines the variables that describe them. Study definitions are written in a Python script using a human-readable API.">study definition</abbr> will be at patient level as usual
and therefore practice variables will be repeated many times for each practice,
and should be aggregated in a later analysis step.</p>


    </div>

</div><p>&nbsp;</p>


<div class="doc doc-object doc-function">


<h4 id="cohortextractor.patients.address_as_of" class="doc doc-heading">
            <code class="highlight language-python"><span class="n">address_as_of</span><span class="p">(</span><span class="n">date</span><span class="p">,</span> <span class="n">returning</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span> <span class="n">round_to_nearest</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span> <span class="n">return_expectations</span><span class="o">=</span><span class="kc">None</span><span class="p">)</span></code>

<a href="#cohortextractor.patients.address_as_of" class="headerlink" title="Permanent link">🔗</a></h4>


    <div class="doc doc-contents first">

        <p>Return patients' address characteristics such as IMD as of a particular date</p>


<p><span class="doc-section-title">Parameters:</span></p>
    <table>
      <thead>
        <tr>
          <th>Name</th>
          <th>Type</th>
          <th>Description</th>
          <th>Default</th>
        </tr>
      </thead>
      <tbody>
          <tr class="doc-section-item">
            <td>
                <code>date</code>
            </td>
            <td>
            </td>
            <td>
              <div class="doc-md-description">
                <p>date of interest as a string with the format <code>YYYY-MM-DD</code>. Filters results to the given date.</p>
              </div>
            </td>
            <td>
                <em>required</em>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>returning</code>
            </td>
            <td>
            </td>
            <td>
              <div class="doc-md-description">
                <p>string indicating value to be returned. Options are:</p>
<ul>
<li><code>index_of_multiple_deprivation</code></li>
<li><code>rural_urban_classification</code></li>
<li><code>msoa</code></li>
</ul>
              </div>
            </td>
            <td>
                  <code>None</code>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>round_to_nearest</code>
            </td>
            <td>
            </td>
            <td>
              <div class="doc-md-description">
                <p>an integer that represents how <code>index_of_multiple_deprivation</code> value are rounded.
Only use when returning is <code>index_of_multiple_deprivation</code></p>
              </div>
            </td>
            <td>
                  <code>None</code>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>return_expectations</code>
            </td>
            <td>
            </td>
            <td>
              <div class="doc-md-description">
                <p>a dict defining the <code>rate</code> and the <code>categories</code> returned with ratios</p>
              </div>
            </td>
            <td>
                  <code>None</code>
            </td>
          </tr>
      </tbody>
    </table>


    <p><span class="doc-section-title">Returns:</span></p>
    <table>
      <thead>
        <tr>
<th>Name</th>          <th>Type</th>
          <th>Description</th>
        </tr>
      </thead>
      <tbody>
          <tr class="doc-section-item">
<td><code>list</code></td>            <td>
            </td>
            <td>
              <div class="doc-md-description">
                <p>of integers for <code>rural_urban_classification</code> and <code>index_of_multiple_deprivation</code>, strings
for <code>msoa</code>.</p>
              </div>
            </td>
          </tr>
          <tr class="doc-section-item">
<td></td>            <td>
            </td>
            <td>
              <div class="doc-md-description">
                <p>rural_urban_classification is encoded (in at least <abbr title="The company behind the SystmOne EHR">TPP</abbr>) as:</p>
              </div>
            </td>
          </tr>
          <tr class="doc-section-item">
<td></td>            <td>
            </td>
            <td>
              <div class="doc-md-description">
                <ul>
<li>1 - Urban major conurbation</li>
</ul>
              </div>
            </td>
          </tr>
          <tr class="doc-section-item">
<td></td>            <td>
            </td>
            <td>
              <div class="doc-md-description">
                <ul>
<li>2 - Urban minor conurbation</li>
</ul>
              </div>
            </td>
          </tr>
          <tr class="doc-section-item">
<td></td>            <td>
            </td>
            <td>
              <div class="doc-md-description">
                <ul>
<li>3 - Urban city and town</li>
</ul>
              </div>
            </td>
          </tr>
          <tr class="doc-section-item">
<td></td>            <td>
            </td>
            <td>
              <div class="doc-md-description">
                <ul>
<li>4 - Urban city and town in a sparse setting</li>
</ul>
              </div>
            </td>
          </tr>
          <tr class="doc-section-item">
<td></td>            <td>
            </td>
            <td>
              <div class="doc-md-description">
                <ul>
<li>5 - Rural town and fringe</li>
</ul>
              </div>
            </td>
          </tr>
          <tr class="doc-section-item">
<td></td>            <td>
            </td>
            <td>
              <div class="doc-md-description">
                <ul>
<li>6 - Rural town and fringe in a sparse setting</li>
</ul>
              </div>
            </td>
          </tr>
          <tr class="doc-section-item">
<td></td>            <td>
            </td>
            <td>
              <div class="doc-md-description">
                <ul>
<li>7 - Rural village and dispersed</li>
</ul>
              </div>
            </td>
          </tr>
          <tr class="doc-section-item">
<td></td>            <td>
            </td>
            <td>
              <div class="doc-md-description">
                <ul>
<li>8 - Rural village and dispersed in a sparse setting</li>
</ul>
              </div>
            </td>
          </tr>
          <tr class="doc-section-item">
<td></td>            <td>
            </td>
            <td>
              <div class="doc-md-description">
                <p><code>index_of_multiple_deprivation</code> (IMD) is a ranking from 1 to 32800 (the number of LSOAs</p>
              </div>
            </td>
          </tr>
          <tr class="doc-section-item">
<td></td>            <td>
            </td>
            <td>
              <div class="doc-md-description">
                <p>in England), where 1 represents most deprived.</p>
              </div>
            </td>
          </tr>
      </tbody>
    </table>


<p><span class="doc-section-title">Raises:</span></p>
    <table>
      <thead>
        <tr>
          <th>Type</th>
          <th>Description</th>
        </tr>
      </thead>
      <tbody>
          <tr class="doc-section-item">
            <td>
                  <code><span title="ValueError">ValueError</span></code>
            </td>
            <td>
              <div class="doc-md-description">
                <p>if unsupported <code>returning</code> argument is provided</p>
              </div>
            </td>
          </tr>
      </tbody>
    </table>
        <p>Example:</p>
<div class="highlight"><pre><span></span><code>This creates a variable called `imd` based on patient address.

    imd=patients.address_as_of(
        &quot;2020-02-29&quot;,
        returning=&quot;index_of_multiple_deprivation&quot;,
        round_to_nearest=100,
        return_expectations={
            &quot;rate&quot;: &quot;universal&quot;,
            &quot;category&quot;: {&quot;ratios&quot;: {&quot;100&quot;: 0.1, &quot;200&quot;: 0.2, &quot;300&quot;: 0.7}},
        },
    )
</code></pre></div>


    </div>

</div><p>&nbsp;</p>
<div class="admonition warning">
<p class="admonition-title">Warning</p>
<p>The original IMD ranking is rounded to the nearest 100 in the OpenSAFELY-<abbr title="The company behind the SystmOne EHR">TPP</abbr> and OpenSAFELY-<abbr title="EMIS Health, formerly known as Egton Medical Information Systems">EMIS</abbr> databases.
The rounded IMD ranking ranges from 0 to 32,800.
If there is no original ranking, then the rounded ranking is -1 in the OpenSAFELY-<abbr title="The company behind the SystmOne EHR">TPP</abbr> database and <code>NULL</code> in the OpenSAFELY-<abbr title="EMIS Health, formerly known as Egton Medical Information Systems">EMIS</abbr> database.</p>
</div>
<div class="admonition warning">
<p class="admonition-title">Warning</p>
<p>Avoid extracting the rounded IMD ranking to a binary format, such as <code>.feather</code> or <code>.dta</code>.
Either nest it within a variable,
such as when <a href="https://docs.opensafely.org/legacy/study-def-tricks/#grouping-imd-by-quintile">grouping rounded IMD by quintile</a>,
or extract it to a non-binary format, such as <code>.csv.gz</code>.</p>
</div>


<div class="doc doc-object doc-function">


<h4 id="cohortextractor.patients.with_gp_consultations" class="doc doc-heading">
            <code class="highlight language-python"><span class="n">with_gp_consultations</span><span class="p">(</span><span class="n">on_or_before</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span> <span class="n">on_or_after</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span> <span class="n">between</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span> <span class="n">find_first_match_in_period</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span> <span class="n">find_last_match_in_period</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span> <span class="n">returning</span><span class="o">=</span><span class="s1">&#39;binary_flag&#39;</span><span class="p">,</span> <span class="n">date_format</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span> <span class="n">return_expectations</span><span class="o">=</span><span class="kc">None</span><span class="p">)</span></code>

<a href="#cohortextractor.patients.with_gp_consultations" class="headerlink" title="Permanent link">🔗</a></h4>


    <div class="doc doc-contents first">

        <div class="admonition warning">
<p class="admonition-title">Warning</p>
</div>
<p>In <abbr title="The company behind the SystmOne EHR">TPP</abbr> this data comes from the "Appointment" table. The data in this table contains
records created when an appointment is made with a GP practice.
It may not capture absolutely all GP/patient interactions,
for example it's uncertain whether an ad-hoc call to a patient would be included.</p>
<p>A <strong>very important</strong> caveat for this data:
there are some circumstances where historical appointment records will be incomplete,
for example when a practice moves from a different <abbr title="Electronic Health Record">EHR</abbr> provider to SystmOne.
If your study could be negatively affected by such missing data, it may be important to use the
<a href="./#cohortextractor.patients.with_complete_gp_consultation_history_between"><code>patients.with_complete_gp_consultation_history_between</code> flag</a>
to only include patients with complete data.</p>
<p>Some further investigation of the appointments data in <abbr title="The company behind the SystmOne EHR">TPP</abbr> can be found in
<a href="https://www.kingsfund.org.uk/blog/2016/05/crisis-general-practice">this King's fund report</a>.</p>


<p><span class="doc-section-title">Parameters:</span></p>
    <table>
      <thead>
        <tr>
          <th>Name</th>
          <th>Type</th>
          <th>Description</th>
          <th>Default</th>
        </tr>
      </thead>
      <tbody>
          <tr class="doc-section-item">
            <td>
                <code>on_or_before</code>
            </td>
            <td>
            </td>
            <td>
              <div class="doc-md-description">
                <p>date of interest as a string with the format <code>YYYY-MM-DD</code>. Filters results to
on or before the given date.</p>
              </div>
            </td>
            <td>
                  <code>None</code>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>on_or_after</code>
            </td>
            <td>
            </td>
            <td>
              <div class="doc-md-description">
                <p>date of interest as a string with the format <code>YYYY-MM-DD</code>. Filters results to
on or after the given date.</p>
              </div>
            </td>
            <td>
                  <code>None</code>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>between</code>
            </td>
            <td>
            </td>
            <td>
              <div class="doc-md-description">
                <p>two dates of interest as a list with each date as a string with the format <code>YYYY-MM-DD</code>.
Filters results to between the two dates provided (inclusive). The two dates must be in chronological order.</p>
              </div>
            </td>
            <td>
                  <code>None</code>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>find_first_match_in_period</code>
            </td>
            <td>
            </td>
            <td>
              <div class="doc-md-description">
                <p>a boolean that indicates if the data returned is first event
if there are multiple matches within the time period</p>
              </div>
            </td>
            <td>
                  <code>None</code>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>find_last_match_in_period</code>
            </td>
            <td>
            </td>
            <td>
              <div class="doc-md-description">
                <p>a boolean that indicates if the data returned is last event
if there are multiple matches within the time period</p>
              </div>
            </td>
            <td>
                  <code>None</code>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>returning</code>
            </td>
            <td>
            </td>
            <td>
              <div class="doc-md-description">
                <p>string indicating value to be returned. Options are:</p>
<ul>
<li><code>binary_flag</code>: indicates if they have had the an event or not</li>
<li><code>date</code>: indicates date of event and used with either find_first_match_in_period or find_last_match_in_period</li>
<li><code>number_of_matches_in_period</code>: counts the events in the period</li>
</ul>
              </div>
            </td>
            <td>
                  <code>&#39;binary_flag&#39;</code>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>date_format</code>
            </td>
            <td>
            </td>
            <td>
              <div class="doc-md-description">
                <p>a string detailing the format of the dates to be returned. It can be <code>YYYY-MM-DD</code>,
<code>YYYY-MM</code> or <code>YYYY</code> and wherever possible the least disclosive data should be returned. i.e returning
only year is less disclosive than a date with day, month and year.</p>
              </div>
            </td>
            <td>
                  <code>None</code>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>return_expectations</code>
            </td>
            <td>
            </td>
            <td>
              <div class="doc-md-description">
                <p>a dictionary defining the incidence and distribution of expected value
within the population in question.</p>
              </div>
            </td>
            <td>
                  <code>None</code>
            </td>
          </tr>
      </tbody>
    </table>


    <p><span class="doc-section-title">Returns:</span></p>
    <table>
      <thead>
        <tr>
<th>Name</th>          <th>Type</th>
          <th>Description</th>
        </tr>
      </thead>
      <tbody>
          <tr class="doc-section-item">
<td><code>list</code></td>            <td>
            </td>
            <td>
              <div class="doc-md-description">
                <p>of integers of <code>1</code> or <code>0</code> if <code>returning</code> argument is set to <code>binary_flag</code>;
list of strings with a date format returned if <code>returning</code> argument is set to <code>date</code>; a list of
integers if <code>returning</code> argument is set to number_of_matches_in_period</p>
              </div>
            </td>
          </tr>
      </tbody>
    </table>
        <p>Example:</p>
<div class="highlight"><pre><span></span><code>A variable called `gp_count` is created that counts number of GP consultation between two dates in
2019.

    gp_count=patients.with_gp_consultations(
        between=[&quot;2019-01-01&quot;, &quot;2020-12-31&quot;],
        returning=&quot;number_of_matches_in_period&quot;,
        return_expectations={
            &quot;int&quot;: {&quot;distribution&quot;: &quot;normal&quot;, &quot;mean&quot;: 6, &quot;stddev&quot;: 3},
            &quot;incidence&quot;: 0.6,
        },
    )
</code></pre></div>


    </div>

</div><p>&nbsp;</p>


<div class="doc doc-object doc-function">


<h4 id="cohortextractor.patients.sex" class="doc doc-heading">
            <code class="highlight language-python"><span class="n">sex</span><span class="p">(</span><span class="n">return_expectations</span><span class="o">=</span><span class="kc">None</span><span class="p">)</span></code>

<a href="#cohortextractor.patients.sex" class="headerlink" title="Permanent link">🔗</a></h4>


    <div class="doc doc-contents first">

        <p>Returns the sex of the patient.</p>


<p><span class="doc-section-title">Parameters:</span></p>
    <table>
      <thead>
        <tr>
          <th>Name</th>
          <th>Type</th>
          <th>Description</th>
          <th>Default</th>
        </tr>
      </thead>
      <tbody>
          <tr class="doc-section-item">
            <td>
                <code>return_expectations</code>
            </td>
            <td>
            </td>
            <td>
              <div class="doc-md-description">
                <p>a dict containing an expectation definition defining a rate and a ratio for sexes</p>
              </div>
            </td>
            <td>
                  <code>None</code>
            </td>
          </tr>
      </tbody>
    </table>


    <p><span class="doc-section-title">Returns:</span></p>
    <table>
      <thead>
        <tr>
<th>Name</th>          <th>Type</th>
          <th>Description</th>
        </tr>
      </thead>
      <tbody>
          <tr class="doc-section-item">
<td><code>list</code></td>            <td>
            </td>
            <td>
              <div class="doc-md-description">
                <p><code>"M"</code> male, <code>"F"</code> female, <code>"I"</code> intersex, or <code>"U"</code> unknown.</p>
              </div>
            </td>
          </tr>
      </tbody>
    </table>


<details class="example" open>
  <summary>Example</summary>
  <p>This creates a variable 'sex' with all patients returning a sex of either "M", "F" or ""</p>
<div class="highlight"><pre><span></span><code>sex=patients.sex(
    return_expectations={
        &quot;rate&quot;: &quot;universal&quot;,
        &quot;category&quot;: {&quot;ratios&quot;: {&quot;M&quot;: 0.49, &quot;F&quot;: 0.51}},
    }
)
</code></pre></div>
</details>

    </div>

</div><p>&nbsp;</p>


<div class="doc doc-object doc-function">


<h4 id="cohortextractor.patients.age_as_of" class="doc doc-heading">
            <code class="highlight language-python"><span class="n">age_as_of</span><span class="p">(</span><span class="n">reference_date</span><span class="p">,</span> <span class="n">return_expectations</span><span class="o">=</span><span class="kc">None</span><span class="p">)</span></code>

<a href="#cohortextractor.patients.age_as_of" class="headerlink" title="Permanent link">🔗</a></h4>


    <div class="doc doc-contents first">

        <p>Returns the patient's age, in whole years, as at <code>reference_date</code>.
Note that the patient's date of birth is rounded down to the first of the month,
and age is derived from this rounded date.</p>
<p>Age can be negative if a patient's date of birth is after the <code>reference_date</code>.</p>


<p><span class="doc-section-title">Parameters:</span></p>
    <table>
      <thead>
        <tr>
          <th>Name</th>
          <th>Type</th>
          <th>Description</th>
          <th>Default</th>
        </tr>
      </thead>
      <tbody>
          <tr class="doc-section-item">
            <td>
                <code>reference_date</code>
            </td>
            <td>
            </td>
            <td>
              <div class="doc-md-description">
                <p>date of interest as a string with the format <code>YYYY-MM-DD</code></p>
              </div>
            </td>
            <td>
                <em>required</em>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>return_expectations</code>
            </td>
            <td>
            </td>
            <td>
              <div class="doc-md-description">
                <p>a dict defining an expectation definition that includes at least a rate
and a distribution. If <code>distribution</code> is defined as "population_ages" it returns likely distribution
based on known UK age bands in 2018 (see file: "uk_population_bands_2018.csv")</p>
              </div>
            </td>
            <td>
                  <code>None</code>
            </td>
          </tr>
      </tbody>
    </table>


    <p><span class="doc-section-title">Returns:</span></p>
    <table>
      <thead>
        <tr>
<th>Name</th>          <th>Type</th>
          <th>Description</th>
        </tr>
      </thead>
      <tbody>
          <tr class="doc-section-item">
<td><code>list</code></td>            <td>
            </td>
            <td>
              <div class="doc-md-description">
                <p>ages as integers</p>
              </div>
            </td>
          </tr>
      </tbody>
    </table>


<details class="example" open>
  <summary>Example</summary>
  <p>This creates a variable "age" with all patient returning an age as an integer:</p>
<div class="highlight"><pre><span></span><code>age=patients.age_as_of(
    &quot;2020-02-01&quot;,
    return_expectations={
        &quot;rate&quot; : &quot;universal&quot;,
        &quot;int&quot; : {&quot;distribution&quot; : &quot;population_ages&quot;}
    }
)
</code></pre></div>
</details>

    </div>

</div><p>&nbsp;</p>


<div class="doc doc-object doc-function">


<h4 id="cohortextractor.patients.date_of_birth" class="doc doc-heading">
            <code class="highlight language-python"><span class="n">date_of_birth</span><span class="p">(</span><span class="n">date_format</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span> <span class="n">return_expectations</span><span class="o">=</span><span class="kc">None</span><span class="p">)</span></code>

<a href="#cohortextractor.patients.date_of_birth" class="headerlink" title="Permanent link">🔗</a></h4>


    <div class="doc doc-contents first">

        <p>Returns date of birth as a string with format "YYYY-MM".</p>


<p><span class="doc-section-title">Parameters:</span></p>
    <table>
      <thead>
        <tr>
          <th>Name</th>
          <th>Type</th>
          <th>Description</th>
          <th>Default</th>
        </tr>
      </thead>
      <tbody>
          <tr class="doc-section-item">
            <td>
                <code>date_format</code>
            </td>
            <td>
            </td>
            <td>
              <div class="doc-md-description">
                <p>a string detailing the format of the dates for date of birth to be returned.
It can be "YYYY-MM" or "YYYY" and wherever possible the least disclosive data should be
returned. i.e returning only year is less disclosive than a date with month and year.</p>
              </div>
            </td>
            <td>
                  <code>None</code>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>return_expectations</code>
            </td>
            <td>
            </td>
            <td>
              <div class="doc-md-description">
                <p>a dictionary containing an expectation definition defining a rate and a distribution</p>
              </div>
            </td>
            <td>
                  <code>None</code>
            </td>
          </tr>
      </tbody>
    </table>


    <p><span class="doc-section-title">Returns:</span></p>
    <table>
      <thead>
        <tr>
<th>Name</th>          <th>Type</th>
          <th>Description</th>
        </tr>
      </thead>
      <tbody>
          <tr class="doc-section-item">
<td><code>list</code></td>            <td>
            </td>
            <td>
              <div class="doc-md-description">
                <p>dates as strings with "YYYY-MM" format</p>
              </div>
            </td>
          </tr>
      </tbody>
    </table>


<p><span class="doc-section-title">Raises:</span></p>
    <table>
      <thead>
        <tr>
          <th>Type</th>
          <th>Description</th>
        </tr>
      </thead>
      <tbody>
          <tr class="doc-section-item">
            <td>
                  <code><span title="ValueError">ValueError</span></code>
            </td>
            <td>
              <div class="doc-md-description">
                <p>if Date of Birth is attempted to be returned with a <code>YYYY-MM-DD</code> format.</p>
              </div>
            </td>
          </tr>
      </tbody>
    </table>
        <p>Example:</p>
<div class="highlight"><pre><span></span><code>This creates a variable `dob` with all patient returning a year and month as a string:

    dob=patients.date_of_birth(
        &quot;YYYY-MM&quot;,
        return_expectations={
            &quot;date&quot;: {&quot;earliest&quot;: &quot;1950-01-01&quot;, &quot;latest&quot;: &quot;today&quot;},
            &quot;rate&quot;: &quot;uniform&quot;,
        }
    )
</code></pre></div>


    </div>

</div><p>&nbsp;</p>


<div class="doc doc-object doc-function">


<h4 id="cohortextractor.patients.most_recent_bmi" class="doc doc-heading">
            <code class="highlight language-python"><span class="n">most_recent_bmi</span><span class="p">(</span><span class="n">on_or_before</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span> <span class="n">on_or_after</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span> <span class="n">between</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span> <span class="n">minimum_age_at_measurement</span><span class="o">=</span><span class="mi">16</span><span class="p">,</span> <span class="n">return_expectations</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span> <span class="n">include_measurement_date</span><span class="o">=</span><span class="kc">False</span><span class="p">,</span> <span class="n">date_format</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span> <span class="n">include_month</span><span class="o">=</span><span class="kc">False</span><span class="p">,</span> <span class="n">include_day</span><span class="o">=</span><span class="kc">False</span><span class="p">)</span></code>

<a href="#cohortextractor.patients.most_recent_bmi" class="headerlink" title="Permanent link">🔗</a></h4>


    <div class="doc doc-contents first">

        <p>Return patients' most recent BMI (in the defined period) either
computed from weight and height measurements or, where they are not
availble, from recorded BMI values. Measurements taken when a patient
was below the minimum age are ignored. The height measurement can be
taken before (but not after) the defined period as long as the patient
was over the minimum age at the time.</p>
<p>The date of the measurement can be obtained using <code>date_of("&lt;bmi-column-name&gt;")</code>.
If the BMI is computed from weight and height then we use the date of the
weight measurement for this.</p>


<p><span class="doc-section-title">Parameters:</span></p>
    <table>
      <thead>
        <tr>
          <th>Name</th>
          <th>Type</th>
          <th>Description</th>
          <th>Default</th>
        </tr>
      </thead>
      <tbody>
          <tr class="doc-section-item">
            <td>
                <code>on_or_before</code>
            </td>
            <td>
            </td>
            <td>
              <div class="doc-md-description">
                <p>date of interest as a string with the format <code>YYYY-MM-DD</code>. Filters results to measurements
on or before the given date.</p>
              </div>
            </td>
            <td>
                  <code>None</code>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>on_or_after</code>
            </td>
            <td>
            </td>
            <td>
              <div class="doc-md-description">
                <p>date of interest as a string with the format <code>YYYY-MM-DD</code>. Filters results to measurements
on or after the given date.</p>
              </div>
            </td>
            <td>
                  <code>None</code>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>between</code>
            </td>
            <td>
            </td>
            <td>
              <div class="doc-md-description">
                <p>two dates of interest as a list with each date as a string with the format <code>YYYY-MM-DD</code>.
Filters results to measurements between the two dates provided (inclusive).
The two dates must be in chronological order.</p>
              </div>
            </td>
            <td>
                  <code>None</code>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>minimum_age_at_measurement</code>
            </td>
            <td>
            </td>
            <td>
              <div class="doc-md-description">
                <p>Measurements taken before this age will not count towards BMI
calculations. It is an integer.</p>
              </div>
            </td>
            <td>
                  <code>16</code>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>return_expectations</code>
            </td>
            <td>
            </td>
            <td>
              <div class="doc-md-description">
                <p>a dictionary defining the incidence and distribution of expected BMI
within the population in question. This is a 3-item key-value dictionary of "date" and "float".
"date" is dictionary itself and should contain the <code>earliest</code> and <code>latest</code> dates needed in the
dummy data. <code>float</code> is a dictionary of <code>distribution</code>, <code>mean</code>, and <code>stddev</code>. These values determine
the shape of the dummy data returned, and the float means a float will be returned rather than an
integer. <code>incidence</code> must have a value and this is what percentage of dummy patients have
a BMI. It needs to be a number between 0 and 1.</p>
              </div>
            </td>
            <td>
                  <code>None</code>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>include_measurement_date</code>
            </td>
            <td>
            </td>
            <td>
              <div class="doc-md-description">
                <p>a boolean indicating if an extra column, named <code>date_of_bmi</code>,
should be included in the output.</p>
              </div>
            </td>
            <td>
                  <code>False</code>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>date_format</code>
            </td>
            <td>
            </td>
            <td>
              <div class="doc-md-description">
                <p>a string detailing the format of the dates to be returned. It can be <code>YYYY-MM-DD</code>,
<code>YYYY-MM</code> or <code>YYYY</code> and wherever possible the least disclosive data should be returned. i.e returning
only year is less disclosive than a date with day, month and year. Only used if
include_measurement_date is <code>True</code></p>
              </div>
            </td>
            <td>
                  <code>None</code>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>include_month</code>
            </td>
            <td>
            </td>
            <td>
              <div class="doc-md-description">
                <p>a boolean indicating if month should be included in addition to year (deprecated: use
<code>date_format</code> instead).</p>
              </div>
            </td>
            <td>
                  <code>False</code>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>include_day</code>
            </td>
            <td>
            </td>
            <td>
              <div class="doc-md-description">
                <p>a boolean indicating if day should be included in addition to year and
month (deprecated: use <code>date_format</code> instead).</p>
              </div>
            </td>
            <td>
                  <code>False</code>
            </td>
          </tr>
      </tbody>
    </table>


    <p><span class="doc-section-title">Returns:</span></p>
    <table>
      <thead>
        <tr>
<th>Name</th>          <th>Type</th>
          <th>Description</th>
        </tr>
      </thead>
      <tbody>
          <tr class="doc-section-item">
<td><code>float</code></td>            <td>
            </td>
            <td>
              <div class="doc-md-description">
                <p>most recent BMI</p>
              </div>
            </td>
          </tr>
      </tbody>
    </table>
        <p>Example:</p>
<div class="highlight"><pre><span></span><code>This creates a variable &quot;bmi&quot; returning a float of the most recent bmi calculated from recorded
height and weight, or from a recorded bmi record. Patient who do not have this information
available do not return a value:

    bmi=patients.most_recent_bmi(
        between=[&quot;2010-02-01&quot;, &quot;2020-01-31&quot;],
        minimum_age_at_measurement=18,
        include_measurement_date=True,
        date_format=&quot;YYYY-MM-DD&quot;,
        return_expectations={
            &quot;date&quot;: {&quot;earliest&quot;: &quot;2010-02-01&quot;, &quot;latest&quot;: &quot;2020-01-31&quot;},
            &quot;float&quot;: {&quot;distribution&quot;: &quot;normal&quot;, &quot;mean&quot;: 28, &quot;stddev&quot;: 8},
            &quot;incidence&quot;: 0.80,
        }
    )
</code></pre></div>


    </div>

</div><p>&nbsp;</p>


<div class="doc doc-object doc-function">


<h4 id="cohortextractor.patients.mean_recorded_value" class="doc doc-heading">
            <code class="highlight language-python"><span class="n">mean_recorded_value</span><span class="p">(</span><span class="n">codelist</span><span class="p">,</span> <span class="n">on_most_recent_day_of_measurement</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span> <span class="n">return_expectations</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span> <span class="n">on_or_before</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span> <span class="n">on_or_after</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span> <span class="n">between</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span> <span class="n">include_measurement_date</span><span class="o">=</span><span class="kc">False</span><span class="p">,</span> <span class="n">date_format</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span> <span class="n">include_month</span><span class="o">=</span><span class="kc">False</span><span class="p">,</span> <span class="n">include_day</span><span class="o">=</span><span class="kc">False</span><span class="p">)</span></code>

<a href="#cohortextractor.patients.mean_recorded_value" class="headerlink" title="Permanent link">🔗</a></h4>


    <div class="doc doc-contents first">

        <p>Return patients' mean recorded value of a numerical value as defined by
a <abbr title="a collection of clinical codes that define a particular condition, event or diagnosis.">codelist</abbr> within the specified period. Optionally, limit to recordings taken on the
most recent day of measurement only.  This is important as it allows
us to account for multiple measurements taken on one day.</p>
<p>The date of the most recent measurement can be included by flagging with date format options.</p>


<p><span class="doc-section-title">Parameters:</span></p>
    <table>
      <thead>
        <tr>
          <th>Name</th>
          <th>Type</th>
          <th>Description</th>
          <th>Default</th>
        </tr>
      </thead>
      <tbody>
          <tr class="doc-section-item">
            <td>
                <code>codelist</code>
            </td>
            <td>
            </td>
            <td>
              <div class="doc-md-description">
                <p>a <abbr title="a collection of clinical codes that define a particular condition, event or diagnosis.">codelist</abbr> for requested value</p>
              </div>
            </td>
            <td>
                <em>required</em>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>on_most_recent_day_of_measurement</code>
            </td>
            <td>
            </td>
            <td>
              <div class="doc-md-description">
                <p>boolean flag for requesting measurements be on most recent date</p>
              </div>
            </td>
            <td>
                  <code>None</code>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>return_expectations</code>
            </td>
            <td>
            </td>
            <td>
              <div class="doc-md-description">
                <p>a dictionary defining the incidence and distribution of expected value
within the population in question. This is a 3-item key-value dictionary of "date" and "float".
"date" is dictionary itself and should contain the <code>earliest</code> and <code>latest</code> dates needed in the
dummy data. <code>float</code> is a dictionary of <code>distribution</code>, <code>mean</code>, and <code>stddev</code>. These values determine
the shape of the dummy data returned, and the float means a float will be returned rather than an
integer. <code>incidence</code> must have a value and this is what percentage of dummy patients have
a value. It needs to be a number between 0 and 1.</p>
              </div>
            </td>
            <td>
                  <code>None</code>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>on_or_before</code>
            </td>
            <td>
            </td>
            <td>
              <div class="doc-md-description">
                <p>date of interest as a string with the format <code>YYYY-MM-DD</code>. Filters results to measurements
on or before the given date.</p>
              </div>
            </td>
            <td>
                  <code>None</code>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>on_or_after</code>
            </td>
            <td>
            </td>
            <td>
              <div class="doc-md-description">
                <p>date of interest as a string with the format <code>YYYY-MM-DD</code>. Filters results to measurements
on or after the given date.</p>
              </div>
            </td>
            <td>
                  <code>None</code>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>between</code>
            </td>
            <td>
            </td>
            <td>
              <div class="doc-md-description">
                <p>two dates of interest as a list with each date as a string with the format <code>YYYY-MM-DD</code>.
Filters results to measurements between the two dates provided (inclusive).
The two dates must be in chronological order.</p>
              </div>
            </td>
            <td>
                  <code>None</code>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>include_measurement_date</code>
            </td>
            <td>
            </td>
            <td>
              <div class="doc-md-description">
                <p>a boolean indicating if an extra column, named <code>&lt;variable_name&gt;_date_measured</code>,
should be included in the output.  This option can only be True when <code>on_most_recent_day_of_measurement</code>
is <code>True</code> (i.e. the value returned is the mean of measurements on a single day).</p>
              </div>
            </td>
            <td>
                  <code>False</code>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>date_format</code>
            </td>
            <td>
            </td>
            <td>
              <div class="doc-md-description">
                <p>a string detailing the format of the dates to be returned. It can be <code>YYYY-MM-DD</code>,
<code>YYYY-MM</code> or <code>YYYY</code> and wherever possible the least disclosive data should be returned. i.e returning
only year is less disclosive than a date with day, month and year. Only used if
include_measurement_date is <code>True</code>.</p>
              </div>
            </td>
            <td>
                  <code>None</code>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>include_month</code>
            </td>
            <td>
            </td>
            <td>
              <div class="doc-md-description">
                <p>a boolean indicating if day should be included in addition to year (deprecated: use
<code>date_format</code> instead).</p>
              </div>
            </td>
            <td>
                  <code>False</code>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>include_day</code>
            </td>
            <td>
            </td>
            <td>
              <div class="doc-md-description">
                <p>a boolean indicating if day should be included in addition to year and
month (deprecated: use <code>date_format</code> instead).</p>
              </div>
            </td>
            <td>
                  <code>False</code>
            </td>
          </tr>
      </tbody>
    </table>


    <p><span class="doc-section-title">Returns:</span></p>
    <table>
      <thead>
        <tr>
<th>Name</th>          <th>Type</th>
          <th>Description</th>
        </tr>
      </thead>
      <tbody>
          <tr class="doc-section-item">
<td><code>float</code></td>            <td>
            </td>
            <td>
              <div class="doc-md-description">
                <p>mean of value</p>
              </div>
            </td>
          </tr>
      </tbody>
    </table>
        <p>Example:</p>
<div class="highlight"><pre><span></span><code>This creates a variable `bp_sys` returning a float of the most recent systolic blood pressure from
the record within the time period. In the event of repeated measurements on the same day, these
are averaged. Patient who do not have this information
available do not return a value.  The date of measurement is returned as `bp_sys_date_measured`, in YYYY-MM format:

    bp_sys=patients.mean_recorded_value(
        systolic_blood_pressure_codes,
        on_most_recent_day_of_measurement=True,
        between=[&quot;2017-02-01&quot;, &quot;2020-01-31&quot;],
        include_measurement_date=True,
        date_format=&quot;YYYY-MM-DD&quot;,
        return_expectations={
            &quot;float&quot;: {&quot;distribution&quot;: &quot;normal&quot;, &quot;mean&quot;: 80, &quot;stddev&quot;: 10},
            &quot;date&quot;: {&quot;earliest&quot;: &quot;2019-02-01&quot;, &quot;latest&quot;: &quot;2020-01-31&quot;},
            &quot;incidence&quot;: 0.95,
        },
    )

Alternatively, the date of measurement can be defined as a separate variable, using `date_of`:

    date_of_bp_sys=patients.date_of(&quot;bp_sys&quot;, date_format=&quot;YYYY-MM-DD&quot;)

This creates a variable returning a float of the mean recorded creatinine level
over a 6 month period:

    creatinine=patients.mean_recorded_value(
        creatinine_codes,
        on_most_recent_day_of_measurement=False,
        between=[&quot;2019-09-16&quot;, &quot;2020-03-15&quot;],
        return_expectations={
            &quot;float&quot;: {&quot;distribution&quot;: &quot;normal&quot;, &quot;mean&quot;: 150, &quot;stddev&quot;: 200},
            &quot;date&quot;: {&quot;earliest&quot;: &quot;2019-09-16&quot;, &quot;latest&quot;: &quot;2020-03-15&quot;},
            &quot;incidence&quot;: 0.75,
        },
    )
</code></pre></div>


    </div>

</div><p>&nbsp;</p>


<div class="doc doc-object doc-function">


<h4 id="cohortextractor.patients.min_recorded_value" class="doc doc-heading">
            <code class="highlight language-python"><span class="n">min_recorded_value</span><span class="p">(</span><span class="n">codelist</span><span class="p">,</span> <span class="n">on_most_recent_day_of_measurement</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span> <span class="n">return_expectations</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span> <span class="n">on_or_before</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span> <span class="n">on_or_after</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span> <span class="n">between</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span> <span class="n">include_measurement_date</span><span class="o">=</span><span class="kc">False</span><span class="p">,</span> <span class="n">date_format</span><span class="o">=</span><span class="kc">None</span><span class="p">)</span></code>

<a href="#cohortextractor.patients.min_recorded_value" class="headerlink" title="Permanent link">🔗</a></h4>


    <div class="doc doc-contents first">

        <p>Return patients' minimum recorded value of a numerical value as defined by
a <abbr title="a collection of clinical codes that define a particular condition, event or diagnosis.">codelist</abbr> within the specified period. Optionally, limit to recordings taken on the
most recent day of measurement only.  This is important as it allows
us to account for multiple measurements taken on one day.</p>
<p>The date of the most recent measurement can be included by flagging with date format options.</p>


<p><span class="doc-section-title">Parameters:</span></p>
    <table>
      <thead>
        <tr>
          <th>Name</th>
          <th>Type</th>
          <th>Description</th>
          <th>Default</th>
        </tr>
      </thead>
      <tbody>
          <tr class="doc-section-item">
            <td>
                <code>codelist</code>
            </td>
            <td>
            </td>
            <td>
              <div class="doc-md-description">
                <p>a <abbr title="a collection of clinical codes that define a particular condition, event or diagnosis.">codelist</abbr> for requested value</p>
              </div>
            </td>
            <td>
                <em>required</em>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>on_most_recent_day_of_measurement</code>
            </td>
            <td>
            </td>
            <td>
              <div class="doc-md-description">
                <p>boolean flag for requesting measurements be on most recent date</p>
              </div>
            </td>
            <td>
                  <code>None</code>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>return_expectations</code>
            </td>
            <td>
            </td>
            <td>
              <div class="doc-md-description">
                <p>a dictionary defining the incidence and distribution of expected value
within the population in question. This is a 3-item key-value dictionary of "date" and "float".
"date" is dictionary itself and should contain the <code>earliest</code> and <code>latest</code> dates needed in the
dummy data. <code>float</code> is a dictionary of <code>distribution</code>, <code>mean</code>, and <code>stddev</code>. These values determine
the shape of the dummy data returned, and the float means a float will be returned rather than an
integer. <code>incidence</code> must have a value and this is what percentage of dummy patients have
a value. It needs to be a number between 0 and 1.</p>
              </div>
            </td>
            <td>
                  <code>None</code>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>on_or_before</code>
            </td>
            <td>
            </td>
            <td>
              <div class="doc-md-description">
                <p>date of interest as a string with the format <code>YYYY-MM-DD</code>. Filters results to measurements
on or before the given date.</p>
              </div>
            </td>
            <td>
                  <code>None</code>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>on_or_after</code>
            </td>
            <td>
            </td>
            <td>
              <div class="doc-md-description">
                <p>date of interest as a string with the format <code>YYYY-MM-DD</code>. Filters results to measurements
on or after the given date.</p>
              </div>
            </td>
            <td>
                  <code>None</code>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>between</code>
            </td>
            <td>
            </td>
            <td>
              <div class="doc-md-description">
                <p>two dates of interest as a list with each date as a string with the format <code>YYYY-MM-DD</code>.
Filters results to measurements between the two dates provided (inclusive).
The two dates must be in chronological order.</p>
              </div>
            </td>
            <td>
                  <code>None</code>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>include_measurement_date</code>
            </td>
            <td>
            </td>
            <td>
              <div class="doc-md-description">
                <p>a boolean indicating if an extra column, named <code>&lt;variable_name&gt;_date_measured</code>,
should be included in the output.  This option can only be True when <code>on_most_recent_day_of_measurement</code>
is <code>True</code> (i.e. the value returned is the minimum measurement taken on a single day).</p>
              </div>
            </td>
            <td>
                  <code>False</code>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>date_format</code>
            </td>
            <td>
            </td>
            <td>
              <div class="doc-md-description">
                <p>a string detailing the format of the dates to be returned. It can be <code>YYYY-MM-DD</code>,
<code>YYYY-MM</code> or <code>YYYY</code> and wherever possible the least disclosive data should be returned. i.e returning
only year is less disclosive than a date with day, month and year. Only used if
include_measurement_date is <code>True</code>.</p>
              </div>
            </td>
            <td>
                  <code>None</code>
            </td>
          </tr>
      </tbody>
    </table>


    <p><span class="doc-section-title">Returns:</span></p>
    <table>
      <thead>
        <tr>
<th>Name</th>          <th>Type</th>
          <th>Description</th>
        </tr>
      </thead>
      <tbody>
          <tr class="doc-section-item">
<td><code>float</code></td>            <td>
            </td>
            <td>
              <div class="doc-md-description">
                <p>min of value</p>
              </div>
            </td>
          </tr>
      </tbody>
    </table>
        <p>Example:</p>
<div class="highlight"><pre><span></span><code>This creates a variable `min_bp_sys` returning a float of the most recent systolic blood pressure from
the record within the time period. In the event of repeated measurements on the same day, the minimum value
is returned. Patient who do not have this information
available do not return a value.  The date of measurement is returned as `min_bp_sys_date_measured`, in YYYY-MM format:

    min_bp_sys=patients.min_recorded_value(
        systolic_blood_pressure_codes,
        on_most_recent_day_of_measurement=True,
        between=[&quot;2017-02-01&quot;, &quot;2020-01-31&quot;],
        include_measurement_date=True,
        date_format=&quot;YYYY-MM-DD&quot;,
        return_expectations={
            &quot;float&quot;: {&quot;distribution&quot;: &quot;normal&quot;, &quot;mean&quot;: 80, &quot;stddev&quot;: 10},
            &quot;date&quot;: {&quot;earliest&quot;: &quot;2019-02-01&quot;, &quot;latest&quot;: &quot;2020-01-31&quot;},
            &quot;incidence&quot;: 0.95,
        },
    )

Alternatively, the date of measurement can be defined as a separate variable, using `date_of`:

    date_of_min_bp=patients.date_of(&quot;min_bp_sys&quot;, date_format=&quot;YYYY-MM-DD&quot;)

This creates a variable returning a float of the minimum recorded creatinine level
over a 6 month period:

    min_creatinine=patients.min_recorded_value(
        creatinine_codes,
        on_most_recent_day_of_measurement=False,
        between=[&quot;2019-09-16&quot;, &quot;2020-03-15&quot;],
        return_expectations={
            &quot;float&quot;: {&quot;distribution&quot;: &quot;normal&quot;, &quot;mean&quot;: 150, &quot;stddev&quot;: 200},
            &quot;date&quot;: {&quot;earliest&quot;: &quot;2019-09-16&quot;, &quot;latest&quot;: &quot;2020-03-15&quot;},
            &quot;incidence&quot;: 0.75,
        },
    )
</code></pre></div>


    </div>

</div><p>&nbsp;</p>


<div class="doc doc-object doc-function">


<h4 id="cohortextractor.patients.max_recorded_value" class="doc doc-heading">
            <code class="highlight language-python"><span class="n">max_recorded_value</span><span class="p">(</span><span class="n">codelist</span><span class="p">,</span> <span class="n">on_most_recent_day_of_measurement</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span> <span class="n">return_expectations</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span> <span class="n">on_or_before</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span> <span class="n">on_or_after</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span> <span class="n">between</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span> <span class="n">include_measurement_date</span><span class="o">=</span><span class="kc">False</span><span class="p">,</span> <span class="n">date_format</span><span class="o">=</span><span class="kc">None</span><span class="p">)</span></code>

<a href="#cohortextractor.patients.max_recorded_value" class="headerlink" title="Permanent link">🔗</a></h4>


    <div class="doc doc-contents first">

        <p>Return patients' maximum recorded value of a numerical value as defined by
a <abbr title="a collection of clinical codes that define a particular condition, event or diagnosis.">codelist</abbr> within the specified period. Optionally, limit to recordings taken on the
most recent day of measurement only.  This is important as it allows
us to account for multiple measurements taken on one day.</p>
<p>The date of the most recent measurement can be included by flagging with date format options.</p>


<p><span class="doc-section-title">Parameters:</span></p>
    <table>
      <thead>
        <tr>
          <th>Name</th>
          <th>Type</th>
          <th>Description</th>
          <th>Default</th>
        </tr>
      </thead>
      <tbody>
          <tr class="doc-section-item">
            <td>
                <code>codelist</code>
            </td>
            <td>
            </td>
            <td>
              <div class="doc-md-description">
                <p>a <abbr title="a collection of clinical codes that define a particular condition, event or diagnosis.">codelist</abbr> for requested value</p>
              </div>
            </td>
            <td>
                <em>required</em>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>on_most_recent_day_of_measurement</code>
            </td>
            <td>
            </td>
            <td>
              <div class="doc-md-description">
                <p>boolean flag for requesting measurements be on most recent date</p>
              </div>
            </td>
            <td>
                  <code>None</code>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>return_expectations</code>
            </td>
            <td>
            </td>
            <td>
              <div class="doc-md-description">
                <p>a dictionary defining the incidence and distribution of expected value
within the population in question. This is a 3-item key-value dictionary of "date" and "float".
"date" is dictionary itself and should contain the <code>earliest</code> and <code>latest</code> dates needed in the
dummy data. <code>float</code> is a dictionary of <code>distribution</code>, <code>mean</code>, and <code>stddev</code>. These values determine
the shape of the dummy data returned, and the float means a float will be returned rather than an
integer. <code>incidence</code> must have a value and this is what percentage of dummy patients have
a value. It needs to be a number between 0 and 1.</p>
              </div>
            </td>
            <td>
                  <code>None</code>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>on_or_before</code>
            </td>
            <td>
            </td>
            <td>
              <div class="doc-md-description">
                <p>date of interest as a string with the format <code>YYYY-MM-DD</code>. Filters results to measurements
on or before the given date.</p>
              </div>
            </td>
            <td>
                  <code>None</code>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>on_or_after</code>
            </td>
            <td>
            </td>
            <td>
              <div class="doc-md-description">
                <p>date of interest as a string with the format <code>YYYY-MM-DD</code>. Filters results to measurements
on or after the given date.</p>
              </div>
            </td>
            <td>
                  <code>None</code>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>between</code>
            </td>
            <td>
            </td>
            <td>
              <div class="doc-md-description">
                <p>two dates of interest as a list with each date as a string with the format <code>YYYY-MM-DD</code>.
Filters results to measurements between the two dates provided (inclusive).
The two dates must be in chronological order.</p>
              </div>
            </td>
            <td>
                  <code>None</code>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>include_measurement_date</code>
            </td>
            <td>
            </td>
            <td>
              <div class="doc-md-description">
                <p>a boolean indicating if an extra column, named <code>&lt;variable_name&gt;_date_measured</code>,
should be included in the output.  This option can only be True when <code>on_most_recent_day_of_measurement</code>
is <code>True</code> (i.e. the value returned is the minimum measurement taken on a single day).</p>
              </div>
            </td>
            <td>
                  <code>False</code>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>date_format</code>
            </td>
            <td>
            </td>
            <td>
              <div class="doc-md-description">
                <p>a string detailing the format of the dates to be returned. It can be <code>YYYY-MM-DD</code>,
<code>YYYY-MM</code> or <code>YYYY</code> and wherever possible the least disclosive data should be returned. i.e returning
only year is less disclosive than a date with day, month and year. Only used if
include_measurement_date is <code>True</code>.</p>
              </div>
            </td>
            <td>
                  <code>None</code>
            </td>
          </tr>
      </tbody>
    </table>


    <p><span class="doc-section-title">Returns:</span></p>
    <table>
      <thead>
        <tr>
<th>Name</th>          <th>Type</th>
          <th>Description</th>
        </tr>
      </thead>
      <tbody>
          <tr class="doc-section-item">
<td><code>float</code></td>            <td>
            </td>
            <td>
              <div class="doc-md-description">
                <p>max of value</p>
              </div>
            </td>
          </tr>
      </tbody>
    </table>
        <p>Example:</p>
<div class="highlight"><pre><span></span><code>This creates a variable `max_bp_sys` returning a float of the most recent systolic blood pressure from
the record within the time period. In the event of repeated measurements on the same day, the maximum
value is returned. Patient who do not have this information
available do not return a value.  The date of measurement is returned as `bp_sys_date_measured`, in YYYY-MM format:

    max_bp_sys=patients.max_recorded_value(
        systolic_blood_pressure_codes,
        on_most_recent_day_of_measurement=True,
        between=[&quot;2017-02-01&quot;, &quot;2020-01-31&quot;],
        include_measurement_date=True,
        date_format=&quot;YYYY-MM-DD&quot;,
        return_expectations={
            &quot;float&quot;: {&quot;distribution&quot;: &quot;normal&quot;, &quot;mean&quot;: 80, &quot;stddev&quot;: 10},
            &quot;date&quot;: {&quot;earliest&quot;: &quot;2019-02-01&quot;, &quot;latest&quot;: &quot;2020-01-31&quot;},
            &quot;incidence&quot;: 0.95,
        },
    )

Alternatively, the date of measurement can be defined as a separate variable, using `date_of`:

    date_of_max_bp=patients.date_of(&quot;max_bp_sys&quot;, date_format=&quot;YYYY-MM-DD&quot;)

This creates a variable returning a float of the maximum recorded creatinine level
over a 6 month period:

    creatinine=patients.max_recorded_value(
        creatinine_codes,
        on_most_recent_day_of_measurement=False,
        between=[&quot;2019-09-16&quot;, &quot;2020-03-15&quot;],
        return_expectations={
            &quot;float&quot;: {&quot;distribution&quot;: &quot;normal&quot;, &quot;mean&quot;: 150, &quot;stddev&quot;: 200},
            &quot;date&quot;: {&quot;earliest&quot;: &quot;2019-09-16&quot;, &quot;latest&quot;: &quot;2020-03-15&quot;},
            &quot;incidence&quot;: 0.75,
        },
    )
</code></pre></div>


    </div>

</div><p>&nbsp;</p>


<div class="doc doc-object doc-function">


<h4 id="cohortextractor.patients.with_these_medications" class="doc doc-heading">
            <code class="highlight language-python"><span class="n">with_these_medications</span><span class="p">(</span><span class="n">codelist</span><span class="p">,</span> <span class="n">return_expectations</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span> <span class="n">on_or_before</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span> <span class="n">on_or_after</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span> <span class="n">between</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span> <span class="n">find_first_match_in_period</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span> <span class="n">find_last_match_in_period</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span> <span class="n">returning</span><span class="o">=</span><span class="s1">&#39;binary_flag&#39;</span><span class="p">,</span> <span class="n">include_date_of_match</span><span class="o">=</span><span class="kc">False</span><span class="p">,</span> <span class="n">date_format</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span> <span class="n">ignore_days_where_these_clinical_codes_occur</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span> <span class="n">episode_defined_as</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span> <span class="n">return_binary_flag</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span> <span class="n">return_number_of_matches_in_period</span><span class="o">=</span><span class="kc">False</span><span class="p">,</span> <span class="n">return_first_date_in_period</span><span class="o">=</span><span class="kc">False</span><span class="p">,</span> <span class="n">return_last_date_in_period</span><span class="o">=</span><span class="kc">False</span><span class="p">,</span> <span class="n">include_month</span><span class="o">=</span><span class="kc">False</span><span class="p">,</span> <span class="n">include_day</span><span class="o">=</span><span class="kc">False</span><span class="p">)</span></code>

<a href="#cohortextractor.patients.with_these_medications" class="headerlink" title="Permanent link">🔗</a></h4>


    <div class="doc doc-contents first">

        <p>Patients who have been prescribed at least one of this list of medications
in the defined period</p>


<p><span class="doc-section-title">Parameters:</span></p>
    <table>
      <thead>
        <tr>
          <th>Name</th>
          <th>Type</th>
          <th>Description</th>
          <th>Default</th>
        </tr>
      </thead>
      <tbody>
          <tr class="doc-section-item">
            <td>
                <code>codelist</code>
            </td>
            <td>
            </td>
            <td>
              <div class="doc-md-description">
                <p>a <abbr title="a collection of clinical codes that define a particular condition, event or diagnosis.">codelist</abbr> for requested medication(s)</p>
              </div>
            </td>
            <td>
                <em>required</em>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>return_expectations</code>
            </td>
            <td>
            </td>
            <td>
              <div class="doc-md-description">
                <p>a dictionary defining the incidence and distribution of expected value
within the population in question. If returning an integer (returning number_of_matches_in_period,
number_of_episodes), this is a 2-item key-value dictionary of <code>int</code> and <code>incidence</code>.
<code>int</code> is a dictionary of <code>distribution</code>, <code>mean</code>, and <code>stddev</code>. These values determine
the shape of the dummy data returned, and the int means a int will be returned rather than a
float. <code>incidence</code> must have a value and this is what percentage of dummy patients have
a value. It needs to be a number between 0 and 1. If returning <code>binary_flag</code> this is a 1-item
dictionary of <code>incidence</code> as described above. If returning either <code>first_date_in_period</code> or
<code>last_date_in_period</code>, this is a 2-item dictionary of <code>date</code> and <code>incidence</code>. <code>date</code> is a dict
of <code>earliest</code> and/or <code>latest</code> date possible.</p>
              </div>
            </td>
            <td>
                  <code>None</code>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>on_or_before</code>
            </td>
            <td>
            </td>
            <td>
              <div class="doc-md-description">
                <p>date of interest as a string with the format <code>YYYY-MM-DD</code>. Filters results to on or
before the given date.</p>
              </div>
            </td>
            <td>
                  <code>None</code>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>on_or_after</code>
            </td>
            <td>
            </td>
            <td>
              <div class="doc-md-description">
                <p>date of interest as a string with the format <code>YYYY-MM-DD</code>. Filters results to
on or after the given date.</p>
              </div>
            </td>
            <td>
                  <code>None</code>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>between</code>
            </td>
            <td>
            </td>
            <td>
              <div class="doc-md-description">
                <p>two dates of interest as a list with each date as a string with the format <code>YYYY-MM-DD</code>.
Filters results to between the two dates provided (inclusive). The two dates must be in chronological order.</p>
              </div>
            </td>
            <td>
                  <code>None</code>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>returning</code>
            </td>
            <td>
            </td>
            <td>
              <div class="doc-md-description">
                <p>string indicating value to be returned. Options are:</p>
<ul>
<li><code>binary_flag</code></li>
<li><code>date</code></li>
<li><code>number_of_matches_in_period</code></li>
<li><code>number_of_episodes</code></li>
<li><code>code</code> (but see warning below)</li>
<li><code>category</code></li>
</ul>
              </div>
            </td>
            <td>
                  <code>&#39;binary_flag&#39;</code>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>find_first_match_in_period</code>
            </td>
            <td>
            </td>
            <td>
              <div class="doc-md-description">
                <p>a boolean indicating if any returned date, code, category, or numeric value
should be based on the first match in the period.
If several matches compare equal, then their IDs are used to break the tie.</p>
              </div>
            </td>
            <td>
                  <code>None</code>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>find_last_match_in_period</code>
            </td>
            <td>
            </td>
            <td>
              <div class="doc-md-description">
                <p>a boolean indicating if any returned date, code, category, or numeric value
should be based on the last match in the period. This is the default behaviour.
If several matches compare equal, then their IDs are used to break the tie.</p>
              </div>
            </td>
            <td>
                  <code>None</code>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>include_date_of_match</code>
            </td>
            <td>
            </td>
            <td>
              <div class="doc-md-description">
                <p>a boolean indicating if an extra column should be included in the output.</p>
              </div>
            </td>
            <td>
                  <code>False</code>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>date_format</code>
            </td>
            <td>
            </td>
            <td>
              <div class="doc-md-description">
                <p>a string detailing the format of the dates to be returned. It can be <code>YYYY-MM-DD</code>,
<code>YYYY-MM</code> or <code>YYYY</code> and wherever possible the least disclosive data should be returned. i.e returning
only year is less disclosive than a date with day, month and year. Only used if include_date_of_match
is <code>True</code></p>
              </div>
            </td>
            <td>
                  <code>None</code>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>ignore_days_where_these_clinical_codes_occur</code>
            </td>
            <td>
            </td>
            <td>
              <div class="doc-md-description">
                <p>a <abbr title="a collection of clinical codes that define a particular condition, event or diagnosis.">codelist</abbr> that contains codes for medications to be
ignored. if a medication is found on this day, the date is not matched even it matches a
code in the main <code><abbr title="a collection of clinical codes that define a particular condition, event or diagnosis.">codelist</abbr></code></p>
              </div>
            </td>
            <td>
                  <code>None</code>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>episode_defined_as</code>
            </td>
            <td>
            </td>
            <td>
              <div class="doc-md-description">
                <p>a string expression indicating how an episode should be defined</p>
              </div>
            </td>
            <td>
                  <code>None</code>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>return_binary_flag</code>
            </td>
            <td>
            </td>
            <td>
              <div class="doc-md-description">
                <p>a bool indicatin if a binary flag should be returned (deprecated: use <code>date_format</code> instead)</p>
              </div>
            </td>
            <td>
                  <code>None</code>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>return_number_of_matches_in_period</code>
            </td>
            <td>
            </td>
            <td>
              <div class="doc-md-description">
                <p>a boolean indicating if the number of matches in a period should be
returned (deprecated: use <code>date_format</code> instead)</p>
              </div>
            </td>
            <td>
                  <code>False</code>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>return_first_date_in_period</code>
            </td>
            <td>
            </td>
            <td>
              <div class="doc-md-description">
                <p>a boolean indicating if the first matches in a period should be
returned (deprecated: use <code>date_format</code> instead)</p>
              </div>
            </td>
            <td>
                  <code>False</code>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>return_last_date_in_period</code>
            </td>
            <td>
            </td>
            <td>
              <div class="doc-md-description">
                <p>a boolean indicating if the last matches in a period should be
returned (deprecated: use <code>date_format</code> instead)</p>
              </div>
            </td>
            <td>
                  <code>False</code>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>include_month</code>
            </td>
            <td>
            </td>
            <td>
              <div class="doc-md-description">
                <p>a boolean indicating if day should be included in addition to year (deprecated: use
<code>date_format</code> instead).</p>
              </div>
            </td>
            <td>
                  <code>False</code>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>include_day</code>
            </td>
            <td>
            </td>
            <td>
              <div class="doc-md-description">
                <p>a boolean indicating if day should be included in addition to year and
month (deprecated: use <code>date_format</code> instead).</p>
              </div>
            </td>
            <td>
                  <code>False</code>
            </td>
          </tr>
      </tbody>
    </table>


    <p><span class="doc-section-title">Returns:</span></p>
    <table>
      <thead>
        <tr>
<th>Name</th>          <th>Type</th>
          <th>Description</th>
        </tr>
      </thead>
      <tbody>
          <tr class="doc-section-item">
<td><code>list</code></td>            <td>
            </td>
            <td>
              <div class="doc-md-description">
                <p>of integers of <code>1</code> or <code>0</code> if <code>returning</code> argument is set to <code>binary_flag</code>, <code>number_of_episodes</code>
or <code>number_of_matches_in_period</code>; list of strings with a date format returned if <code>returning</code>
argument is set to <code>first_date_in_period</code> or <code>last_date_in_period</code>.</p>
              </div>
            </td>
          </tr>
      </tbody>
    </table>
        <p>Example:</p>
<div class="highlight"><pre><span></span><code>This creates a variable `exacerbation_count` returning an int of the number of episodes of oral
steroids being prescribed within the time period where a prescription is counted as part of the same
episode if it falls within 28 days of a previous prescription. Days where oral steroids
are prescribed on the same day as a COPD review are also ignored as may not represent true exacerbations.

    exacerbation_count=patients.with_these_medications(
        oral_steroid_med_codes,
        between=[&quot;2019-03-01&quot;, &quot;2020-02-29&quot;],
        ignore_days_where_these_clinical_codes_occur=copd_reviews,
        returning=&quot;number_of_episodes&quot;,
        episode_defined_as=&quot;series of events each &lt;= 28 days apart&quot;,
        return_expectations={
            &quot;int&quot;: {&quot;distribution&quot;: &quot;normal&quot;, &quot;mean&quot;: 2, &quot;stddev&quot;: 1},
            &quot;incidence&quot;: 0.2,
        },
    )
</code></pre></div>


    </div>

</div><p>&nbsp;</p>
<div class="admonition warning">
<p class="admonition-title">Warning</p>
<p>dm+d codes for Virtual Medicinal Products (VMPs) can change.
cohort-extractor handles this by automatically expanding a medication <abbr title="a collection of clinical codes that define a particular condition, event or diagnosis.">codelist</abbr>
to include all current and previous codes of any VMPs in the <abbr title="a collection of clinical codes that define a particular condition, event or diagnosis.">codelist</abbr>.
However, this means that when a VMP code has changed, a query using
<code>patients.with_these_medications(<abbr title="a collection of clinical codes that define a particular condition, event or diagnosis.">codelist</abbr>, returning="code", ...)</code>
might return a code that is not in the provided <abbr title="a collection of clinical codes that define a particular condition, event or diagnosis.">codelist</abbr>.</p>
</div>


<div class="doc doc-object doc-function">


<h4 id="cohortextractor.patients.with_these_clinical_events" class="doc doc-heading">
            <code class="highlight language-python"><span class="n">with_these_clinical_events</span><span class="p">(</span><span class="n">codelist</span><span class="p">,</span> <span class="n">return_expectations</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span> <span class="n">on_or_before</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span> <span class="n">on_or_after</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span> <span class="n">between</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span> <span class="n">find_first_match_in_period</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span> <span class="n">find_last_match_in_period</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span> <span class="n">returning</span><span class="o">=</span><span class="s1">&#39;binary_flag&#39;</span><span class="p">,</span> <span class="n">include_date_of_match</span><span class="o">=</span><span class="kc">False</span><span class="p">,</span> <span class="n">date_format</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span> <span class="n">ignore_missing_values</span><span class="o">=</span><span class="kc">False</span><span class="p">,</span> <span class="n">ignore_days_where_these_codes_occur</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span> <span class="n">episode_defined_as</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span> <span class="n">return_binary_flag</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span> <span class="n">return_number_of_matches_in_period</span><span class="o">=</span><span class="kc">False</span><span class="p">,</span> <span class="n">return_first_date_in_period</span><span class="o">=</span><span class="kc">False</span><span class="p">,</span> <span class="n">return_last_date_in_period</span><span class="o">=</span><span class="kc">False</span><span class="p">,</span> <span class="n">include_month</span><span class="o">=</span><span class="kc">False</span><span class="p">,</span> <span class="n">include_day</span><span class="o">=</span><span class="kc">False</span><span class="p">)</span></code>

<a href="#cohortextractor.patients.with_these_clinical_events" class="headerlink" title="Permanent link">🔗</a></h4>


    <div class="doc doc-contents first">

        <p>Patients who have had at least one of these clinical events in the defined
period. This is used for many types of events in primary care, such as
symptoms, test results, diagnoses, investigations, and some demographic
and social characteristics. NB: for prescriptions and vaccinations, use
the more specific queries available in cohort-extractor. For onward referrals,
data is incomplete and should not be relied upon.</p>


<p><span class="doc-section-title">Parameters:</span></p>
    <table>
      <thead>
        <tr>
          <th>Name</th>
          <th>Type</th>
          <th>Description</th>
          <th>Default</th>
        </tr>
      </thead>
      <tbody>
          <tr class="doc-section-item">
            <td>
                <code>codelist</code>
            </td>
            <td>
            </td>
            <td>
              <div class="doc-md-description">
                <p>a <abbr title="a collection of clinical codes that define a particular condition, event or diagnosis.">codelist</abbr> for requested event(s)</p>
              </div>
            </td>
            <td>
                <em>required</em>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>return_expectations</code>
            </td>
            <td>
            </td>
            <td>
              <div class="doc-md-description">
                <p>a dictionary defining the incidence and distribution of expected value
within the population in question. If returning an integer (<code>returning=number_of_matches_in_period</code>
or <code>returning=number_of_episodes</code>), this is a 2-item key-value dictionary of <code>int</code> and <code>incidence</code>.
<code>int</code> is a dictionary of <code>distribution</code>, <code>mean</code>, and <code>stddev</code>. These values determine
the shape of the dummy data returned, and the int means a int will be returned rather than a
float. <code>incidence</code> must have a value and this is what percentage of dummy patients have
a value. It needs to be a number between 0 and 1. If returning <code>binary_flag</code> this is a 1-item
dictionary of <code>incidence</code> as described above. If returning either <code>first_date_in_period</code> or
<code>last_date_in_period</code>, this is a 2-item dictionary of <code>date</code> and <code>incidence</code>. <code>date</code> is a dict
of <code>earliest</code> and/or <code>latest</code> date possible.</p>
              </div>
            </td>
            <td>
                  <code>None</code>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>on_or_before</code>
            </td>
            <td>
            </td>
            <td>
              <div class="doc-md-description">
                <p>date of interest as a string with the format <code>YYYY-MM-DD</code>. Filters results to on or
before the given date.</p>
              </div>
            </td>
            <td>
                  <code>None</code>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>on_or_after</code>
            </td>
            <td>
            </td>
            <td>
              <div class="doc-md-description">
                <p>date of interest as a string with the format <code>YYYY-MM-DD</code>. Filters results to
on or after the given date.</p>
              </div>
            </td>
            <td>
                  <code>None</code>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>between</code>
            </td>
            <td>
            </td>
            <td>
              <div class="doc-md-description">
                <p>two dates of interest as a list with each date as a string with the format <code>YYYY-MM-DD</code>.
Filters results to between the two dates provided (inclusive).
The two dates must be in chronological order.</p>
              </div>
            </td>
            <td>
                  <code>None</code>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>returning</code>
            </td>
            <td>
            </td>
            <td>
              <div class="doc-md-description">
                <p>string indicating value to be returned. Options are:</p>
<ul>
<li><code>binary_flag</code></li>
<li><code>date</code></li>
<li><code>number_of_matches_in_period</code></li>
<li><code>number_of_episodes</code></li>
<li><code>code</code></li>
<li><code>category</code></li>
<li><code>numeric_value</code> (see also <a href="./#cohortextractor.patients.comparator_from">comparators</a>
   and <a href="./#cohortextractor.patients.reference_range_lower_bound_from">reference ranges</a>)</li>
</ul>
              </div>
            </td>
            <td>
                  <code>&#39;binary_flag&#39;</code>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>find_first_match_in_period</code>
            </td>
            <td>
            </td>
            <td>
              <div class="doc-md-description">
                <p>a boolean indicating if any returned date, code, category, or numeric value
should be based on the first match in the period.
If several matches compare equal, then their IDs are used to break the tie.</p>
              </div>
            </td>
            <td>
                  <code>None</code>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>find_last_match_in_period</code>
            </td>
            <td>
            </td>
            <td>
              <div class="doc-md-description">
                <p>a boolean indicating if any returned date, code, category, or numeric value
should be based on the last match in the period. This is the default behaviour.
If several matches compare equal, then their IDs are used to break the tie.</p>
              </div>
            </td>
            <td>
                  <code>None</code>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>include_date_of_match</code>
            </td>
            <td>
            </td>
            <td>
              <div class="doc-md-description">
                <p>a boolean indicating if an extra column should be included in the output.</p>
              </div>
            </td>
            <td>
                  <code>False</code>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>date_format</code>
            </td>
            <td>
            </td>
            <td>
              <div class="doc-md-description">
                <p>a string detailing the format of the dates to be returned. It can be <code>YYYY-MM-DD</code>,
<code>YYYY-MM</code> or <code>YYYY</code> and wherever possible the least disclosive data should be returned. i.e returning
only year is less disclosive than a date with day, month and year. Only used if include_date_of_match
is <code>True</code></p>
              </div>
            </td>
            <td>
                  <code>None</code>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>ignore_days_where_these_codes_occur</code>
            </td>
            <td>
            </td>
            <td>
              <div class="doc-md-description">
                <p>a <abbr title="a collection of clinical codes that define a particular condition, event or diagnosis.">codelist</abbr> that contains codes for events to be
ignored. if a events is found on this day, the date is not matched even it matches a
code in the main <code><abbr title="a collection of clinical codes that define a particular condition, event or diagnosis.">codelist</abbr></code></p>
              </div>
            </td>
            <td>
                  <code>None</code>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>episode_defined_as</code>
            </td>
            <td>
            </td>
            <td>
              <div class="doc-md-description">
                <p>a string expression indicating how an episode should be defined</p>
              </div>
            </td>
            <td>
                  <code>None</code>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>ignore_missing_values</code>
            </td>
            <td>
            </td>
            <td>
              <div class="doc-md-description">
                <p>ignore events where the value is missing or zero.  We are
unable to distinguish between zeros and null values due to limitations in
how the data is recorded in <abbr title="The company behind the SystmOne EHR">TPP</abbr>.</p>
              </div>
            </td>
            <td>
                  <code>False</code>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>return_binary_flag</code>
            </td>
            <td>
            </td>
            <td>
              <div class="doc-md-description">
                <p>a boolean indicating if the number of matches in a period should be
returned (deprecated: use <code>date_format</code> instead),</p>
              </div>
            </td>
            <td>
                  <code>None</code>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>return_number_of_matches_in_period</code>
            </td>
            <td>
            </td>
            <td>
              <div class="doc-md-description">
                <p>a boolean indicating if the number of matches in a period should be
returned (deprecated: use <code>date_format</code> instead)</p>
              </div>
            </td>
            <td>
                  <code>False</code>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>return_first_date_in_period</code>
            </td>
            <td>
            </td>
            <td>
              <div class="doc-md-description">
                <p>a boolean indicating if the first matches in a period should be
returned (deprecated: use <code>date_format</code> instead)</p>
              </div>
            </td>
            <td>
                  <code>False</code>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>return_last_date_in_period</code>
            </td>
            <td>
            </td>
            <td>
              <div class="doc-md-description">
                <p>a boolean indicating if the last matches in a period should be
returned (deprecated: use <code>date_format</code> instead)</p>
              </div>
            </td>
            <td>
                  <code>False</code>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>include_month</code>
            </td>
            <td>
            </td>
            <td>
              <div class="doc-md-description">
                <p>a boolean indicating if day should be included in addition to year (deprecated: use
<code>date_format</code> instead).</p>
              </div>
            </td>
            <td>
                  <code>False</code>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>include_day</code>
            </td>
            <td>
            </td>
            <td>
              <div class="doc-md-description">
                <p>a boolean indicating if day should be included in addition to year and
month (deprecated: use <code>date_format</code> instead).</p>
              </div>
            </td>
            <td>
                  <code>False</code>
            </td>
          </tr>
      </tbody>
    </table>


    <p><span class="doc-section-title">Returns:</span></p>
    <table>
      <thead>
        <tr>
<th>Name</th>          <th>Type</th>
          <th>Description</th>
        </tr>
      </thead>
      <tbody>
          <tr class="doc-section-item">
<td><code>list</code></td>            <td>
            </td>
            <td>
              <div class="doc-md-description">
                <p>of integers of <code>1</code> or <code>0</code> if <code>returning</code> argument is set to <code>binary_flag</code>, <code>number_of_episodes</code>
or <code>number_of_matches_in_period</code>; list of strings with a date format returned if <code>returning</code>
argument is set to <code>first_date_in_period</code> or <code>last_date_in_period</code>. a list of strings with a category
represented in an extra column in the <abbr title="a collection of clinical codes that define a particular condition, event or diagnosis.">codelist</abbr> object <code>category</code> is returned.</p>
              </div>
            </td>
          </tr>
      </tbody>
    </table>
        <p>Example:</p>
<div class="highlight"><pre><span></span><code>This creates a variable `haem_cancer` returning the first date of a diagnosis of haematology
malignancy within the time period.

    haem_cancer=patients.with_these_clinical_events(
        haem_cancer_codes,
        between=[&quot;2015-03-01&quot;, &quot;2020-02-29&quot;],
        returning=&quot;date&quot;,
        find_first_match_in_period=True,
        return_expectations={&quot;date&quot;: {earliest; &quot;2015-03-01&quot;, &quot;latest&quot;: &quot;2020-02-29&quot;}},
    )
</code></pre></div>


    </div>

</div><p>&nbsp;</p>


<div class="doc doc-object doc-function">


<h4 id="cohortextractor.patients.comparator_from" class="doc doc-heading">
            <code class="highlight language-python"><span class="n">comparator_from</span><span class="p">(</span><span class="n">source</span><span class="p">,</span> <span class="n">return_expectations</span><span class="o">=</span><span class="kc">None</span><span class="p">)</span></code>

<a href="#cohortextractor.patients.comparator_from" class="headerlink" title="Permanent link">🔗</a></h4>


    <div class="doc doc-contents first">

        <p>Fetch the comparator (<code>&lt;</code>, <code>&gt;=</code>, <code>=</code> etc) associated with a numeric value.</p>
<p>Where a lab result is returned as e.g. <code>&lt;9.5</code> the numeric_value component
will contain only the value 9.5 and you will need to use this function to
fetch the comparator into a separate column.</p>


<p><span class="doc-section-title">Parameters:</span></p>
    <table>
      <thead>
        <tr>
          <th>Name</th>
          <th>Type</th>
          <th>Description</th>
          <th>Default</th>
        </tr>
      </thead>
      <tbody>
          <tr class="doc-section-item">
            <td>
                <code>source</code>
            </td>
            <td>
            </td>
            <td>
              <div class="doc-md-description">
                <p>name of a numeric value column i.e. a column that uses
<code>with_these_clinical_events(returning="numeric_value")</code></p>
              </div>
            </td>
            <td>
                <em>required</em>
            </td>
          </tr>
      </tbody>
    </table>


    <p><span class="doc-section-title">Returns:</span></p>
    <table>
      <thead>
        <tr>
<th>Name</th>          <th>Type</th>
          <th>Description</th>
        </tr>
      </thead>
      <tbody>
          <tr class="doc-section-item">
<td><code>list</code></td>            <td>
            </td>
            <td>
              <div class="doc-md-description">
                <p>of strings from the set: <code>~</code>, <code>=</code>, <code>&gt;=</code>, <code>&gt;</code>, <code>&lt;</code>, <code>&lt;=</code></p>
              </div>
            </td>
          </tr>
      </tbody>
    </table>
        <p>Example:</p>
<div class="highlight"><pre><span></span><code>Fetch each patient&#39;s latest HbA1c and the associated comparator:

    latest_hba1c=patients.with_these_clinical_events(
        hba1c_codes,
        returning=&quot;numeric_value&quot;, find_last_match_in_period=True
    ),
    hba1c_comparator=patients.comparator_from(&quot;latest_hba1c&quot;),
</code></pre></div>


    </div>

</div><p>&nbsp;</p>


<div class="doc doc-object doc-function">


<h4 id="cohortextractor.patients.reference_range_lower_bound_from" class="doc doc-heading">
            <code class="highlight language-python"><span class="n">reference_range_lower_bound_from</span><span class="p">(</span><span class="n">source</span><span class="p">,</span> <span class="n">return_expectations</span><span class="o">=</span><span class="kc">None</span><span class="p">)</span></code>

<a href="#cohortextractor.patients.reference_range_lower_bound_from" class="headerlink" title="Permanent link">🔗</a></h4>


    <div class="doc doc-contents first">

        <p>Fetch the lower bound of the reference range associated with the numeric
value from a lab result.</p>


<p><span class="doc-section-title">Parameters:</span></p>
    <table>
      <thead>
        <tr>
          <th>Name</th>
          <th>Type</th>
          <th>Description</th>
          <th>Default</th>
        </tr>
      </thead>
      <tbody>
          <tr class="doc-section-item">
            <td>
                <code>source</code>
            </td>
            <td>
            </td>
            <td>
              <div class="doc-md-description">
                <p>name of a numeric value column i.e. a column that uses
<code>with_these_clinical_events(returning="numeric_value")</code></p>
              </div>
            </td>
            <td>
                <em>required</em>
            </td>
          </tr>
      </tbody>
    </table>


    <p><span class="doc-section-title">Returns:</span></p>
    <table>
      <thead>
        <tr>
<th>Name</th>          <th>Type</th>
          <th>Description</th>
        </tr>
      </thead>
      <tbody>
          <tr class="doc-section-item">
<td><code>list</code></td>            <td>
            </td>
            <td>
              <div class="doc-md-description">
                <p>of floats (note a value of <code>-1</code> indicates "no lower bound")</p>
              </div>
            </td>
          </tr>
      </tbody>
    </table>
        <p>Example:</p>
<div class="highlight"><pre><span></span><code>Fetch each patient&#39;s latest HbA1c and the lower bound of the associated
reference range:

    latest_hba1c=patients.with_these_clinical_events(
        hba1c_codes,
        returning=&quot;numeric_value&quot;, find_last_match_in_period=True
    ),
    hba1c_ref_range_lower=patients.reference_range_lower_bound_from(
        &quot;latest_hba1c&quot;
    ),
</code></pre></div>


    </div>

</div><p>&nbsp;</p>


<div class="doc doc-object doc-function">


<h4 id="cohortextractor.patients.reference_range_upper_bound_from" class="doc doc-heading">
            <code class="highlight language-python"><span class="n">reference_range_upper_bound_from</span><span class="p">(</span><span class="n">source</span><span class="p">,</span> <span class="n">return_expectations</span><span class="o">=</span><span class="kc">None</span><span class="p">)</span></code>

<a href="#cohortextractor.patients.reference_range_upper_bound_from" class="headerlink" title="Permanent link">🔗</a></h4>


    <div class="doc doc-contents first">

        <p>Fetch the upper bound of the reference range associated with the numeric
value from a lab result.</p>


<p><span class="doc-section-title">Parameters:</span></p>
    <table>
      <thead>
        <tr>
          <th>Name</th>
          <th>Type</th>
          <th>Description</th>
          <th>Default</th>
        </tr>
      </thead>
      <tbody>
          <tr class="doc-section-item">
            <td>
                <code>source</code>
            </td>
            <td>
            </td>
            <td>
              <div class="doc-md-description">
                <p>name of a numeric value column i.e. a column that uses
<code>with_these_clinical_events(returning="numeric_value")</code></p>
              </div>
            </td>
            <td>
                <em>required</em>
            </td>
          </tr>
      </tbody>
    </table>


    <p><span class="doc-section-title">Returns:</span></p>
    <table>
      <thead>
        <tr>
<th>Name</th>          <th>Type</th>
          <th>Description</th>
        </tr>
      </thead>
      <tbody>
          <tr class="doc-section-item">
<td><code>list</code></td>            <td>
            </td>
            <td>
              <div class="doc-md-description">
                <p>of floats (note a value of <code>-1</code> indicates "no upper bound")</p>
              </div>
            </td>
          </tr>
      </tbody>
    </table>
        <p>Example:</p>
<div class="highlight"><pre><span></span><code>Fetch each patient&#39;s latest HbA1c and the upper bound of the associated
reference range:

    latest_hba1c=patients.with_these_clinical_events(
        hba1c_codes,
        returning=&quot;numeric_value&quot;, find_last_match_in_period=True
    ),
    hba1c_ref_range_upper=patients.reference_range_upper_bound_from(
        &quot;latest_hba1c&quot;
    ),
</code></pre></div>


    </div>

</div><p>&nbsp;</p>


<div class="doc doc-object doc-function">


<h4 id="cohortextractor.patients.with_death_recorded_in_primary_care" class="doc doc-heading">
            <code class="highlight language-python"><span class="n">with_death_recorded_in_primary_care</span><span class="p">(</span><span class="n">on_or_before</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span> <span class="n">on_or_after</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span> <span class="n">between</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span> <span class="n">returning</span><span class="o">=</span><span class="s1">&#39;binary_flag&#39;</span><span class="p">,</span> <span class="n">date_format</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span> <span class="n">return_expectations</span><span class="o">=</span><span class="kc">None</span><span class="p">)</span></code>

<a href="#cohortextractor.patients.with_death_recorded_in_primary_care" class="headerlink" title="Permanent link">🔗</a></h4>


    <div class="doc doc-contents first">

        <p>Identify patients with a date-of-death in their primary care record.</p>
<p>There is generally a lag between the death being recorded in <abbr title="Office for National Statistics - the UK's largest independent producer of official statistics and the recognised national statistical institute of the UK">ONS</abbr> data and
appearing in the primary care record, but the date itself is usually
reliable when it appears. By contrast, cause of death is often not accurate
in the primary care record so we don't make it available to query here.</p>


<p><span class="doc-section-title">Parameters:</span></p>
    <table>
      <thead>
        <tr>
          <th>Name</th>
          <th>Type</th>
          <th>Description</th>
          <th>Default</th>
        </tr>
      </thead>
      <tbody>
          <tr class="doc-section-item">
            <td>
                <code>on_or_before</code>
            </td>
            <td>
            </td>
            <td>
              <div class="doc-md-description">
                <p>date of interest as a string with the format <code>YYYY-MM-DD</code>. Filters results
on or before the given date.</p>
              </div>
            </td>
            <td>
                  <code>None</code>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>on_or_after</code>
            </td>
            <td>
            </td>
            <td>
              <div class="doc-md-description">
                <p>date of interest as a string with the format <code>YYYY-MM-DD</code>. Filters results
on or after the given date.</p>
              </div>
            </td>
            <td>
                  <code>None</code>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>between</code>
            </td>
            <td>
            </td>
            <td>
              <div class="doc-md-description">
                <p>two dates of interest as a list with each date as a string with the format <code>YYYY-MM-DD</code>.
Filters results to  between the two dates provided (inclusive).
The two dates must be in chronological order.</p>
              </div>
            </td>
            <td>
                  <code>None</code>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>returning</code>
            </td>
            <td>
            </td>
            <td>
              <div class="doc-md-description">
                <p>string indicating value to be returned. Options are:</p>
<ul>
<li><code>date_of_death</code>: Date of death</li>
<li><code>binary_flag</code>: If they died or not</li>
</ul>
              </div>
            </td>
            <td>
                  <code>&#39;binary_flag&#39;</code>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>date_format</code>
            </td>
            <td>
            </td>
            <td>
              <div class="doc-md-description">
                <p>a string detailing the format of the dates to be returned. It can be <code>YYYY-MM-DD</code>,
<code>YYYY-MM</code> or <code>YYYY</code> and wherever possible the least disclosive data should be returned. i.e returning
only year is less disclosive than a date with day, month and year.</p>
              </div>
            </td>
            <td>
                  <code>None</code>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>return_expectations</code>
            </td>
            <td>
            </td>
            <td>
              <div class="doc-md-description">
                <p>a dictionary defining the incidence and distribution of expected value
within the population in question.</p>
              </div>
            </td>
            <td>
                  <code>None</code>
            </td>
          </tr>
      </tbody>
    </table>


    <p><span class="doc-section-title">Returns:</span></p>
    <table>
      <thead>
        <tr>
<th>Name</th>          <th>Type</th>
          <th>Description</th>
        </tr>
      </thead>
      <tbody>
          <tr class="doc-section-item">
<td><code>list</code></td>            <td>
            </td>
            <td>
              <div class="doc-md-description">
                <p>of integers of <code>1</code> or <code>0</code> if <code>returning</code> argument is set to <code>binary_flag</code>;
list of strings with a date format returned if <code>returning</code> argument is set to <code>date_of_death</code></p>
              </div>
            </td>
          </tr>
      </tbody>
    </table>
        <p>Example:</p>
<div class="highlight"><pre><span></span><code>A variable called `died_date_gp` is created that returns the date of death for
any patients have died in the GP dataset.

    died_date_gp=patients.with_death_recorded_in_primary_care(
        on_or_after=&quot;2020-02-01&quot;,
        returning=&quot;date_of_death&quot;,
        return_expectations={
            &quot;date&quot;: {&quot;earliest&quot; : &quot;2020-02-01&quot;},
            &quot;rate&quot; : &quot;exponential_increase&quot;
        },
    ),
</code></pre></div>


    </div>

</div><p>&nbsp;</p>


<div class="doc doc-object doc-function">


<h4 id="cohortextractor.patients.care_home_status_as_of" class="doc doc-heading">
            <code class="highlight language-python"><span class="n">care_home_status_as_of</span><span class="p">(</span><span class="n">date</span><span class="p">,</span> <span class="n">categorised_as</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span> <span class="n">return_expectations</span><span class="o">=</span><span class="kc">None</span><span class="p">)</span></code>

<a href="#cohortextractor.patients.care_home_status_as_of" class="headerlink" title="Permanent link">🔗</a></h4>


    <div class="doc doc-contents first">

        <p><abbr title="The company behind the SystmOne EHR">TPP</abbr> have attempted to match patient addresses to care homes as stored in
the CQC database. At its most simple this query returns a boolean
indicating whether the patient's address (as of the supplied time) matched
with a care home.</p>
<p>It is also possible return a more complex categorisation based on
attributes of the care homes in the CQC database, which can be freely
downloaded here:
https://www.cqc.org.uk/about-us/transparency/using-cqc-data</p>


<details class="at-present-the-only-imported-fields-are" open>
  <summary>At present the only imported fields are</summary>
  <p>LocationRequiresNursing
LocationDoesNotRequireNursing</p>
</details>        <p>But we can ask for more fields to be imported if needed.</p>
<p>The <code>categorised_as</code> argument acts in effectively the same way as for the
<code>categorised_as</code> function except that the only columns that can be referred
to are those belonging to the care home table (i.e. the two nursing fields
above) and the boolean <code>IsPotentialCareHome</code></p>


<p><span class="doc-section-title">Parameters:</span></p>
    <table>
      <thead>
        <tr>
          <th>Name</th>
          <th>Type</th>
          <th>Description</th>
          <th>Default</th>
        </tr>
      </thead>
      <tbody>
          <tr class="doc-section-item">
            <td>
                <code>date</code>
            </td>
            <td>
            </td>
            <td>
              <div class="doc-md-description">
                <p>date of interest as a string with the format <code>YYYY-MM-DD</code>. Filters results to the given date</p>
              </div>
            </td>
            <td>
                <em>required</em>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>categorised_as</code>
            </td>
            <td>
            </td>
            <td>
              <div class="doc-md-description">
                <p>a logic expression that applies an algorithm to specific variables to create categories</p>
              </div>
            </td>
            <td>
                  <code>None</code>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>return_expectations</code>
            </td>
            <td>
            </td>
            <td>
              <div class="doc-md-description">
                <p>a dict defining the <code>rate</code> and the <code>categories</code> returned with ratios</p>
              </div>
            </td>
            <td>
                  <code>None</code>
            </td>
          </tr>
      </tbody>
    </table>


    <p><span class="doc-section-title">Returns:</span></p>
    <table>
      <thead>
        <tr>
<th>Name</th>          <th>Type</th>
          <th>Description</th>
        </tr>
      </thead>
      <tbody>
          <tr class="doc-section-item">
<td><code>list</code></td>            <td>
            </td>
            <td>
              <div class="doc-md-description">
                <p>of strings which each letter representing a category as defined by the algorithm</p>
              </div>
            </td>
          </tr>
      </tbody>
    </table>
        <p>Example:</p>
<div class="highlight"><pre><span></span><code>This creates a variable called `care_home_type` which contains a 2
letter string which represents a type of care home environment. If the
address is not valid, it defaults to an empty string.

    care_home_type=patients.care_home_status_as_of(
        &quot;2020-02-01&quot;,
        categorised_as={
            &quot;PC&quot;:
            &quot;&quot;&quot;
              IsPotentialCareHome
              AND LocationDoesNotRequireNursing=&#39;Y&#39;
              AND LocationRequiresNursing=&#39;N&#39;
            &quot;&quot;&quot;,
            &quot;PN&quot;:
            &quot;&quot;&quot;
              IsPotentialCareHome
              AND LocationDoesNotRequireNursing=&#39;N&#39;
              AND LocationRequiresNursing=&#39;Y&#39;
            &quot;&quot;&quot;,
            &quot;PS&quot;: &quot;IsPotentialCareHome&quot;,
            &quot;PR&quot;: &quot;NOT IsPotentialCareHome&quot;,
            &quot;&quot;: &quot;DEFAULT&quot;,
        },
        return_expectations={
            &quot;rate&quot;: &quot;universal&quot;,
            &quot;category&quot;: {&quot;ratios&quot;: {&quot;PC&quot;: 0.05, &quot;PN&quot;: 0.05, &quot;PS&quot;: 0.05, &quot;PR&quot;: 0.84, &quot;&quot;: 0.01},},
        },
    ),
</code></pre></div>


    </div>

</div><p>&nbsp;</p>


<div class="doc doc-object doc-function">


<h4 id="cohortextractor.patients.with_tpp_vaccination_record" class="doc doc-heading">
            <code class="highlight language-python"><span class="n">with_tpp_vaccination_record</span><span class="p">(</span><span class="n">target_disease_matches</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span> <span class="n">product_name_matches</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span> <span class="n">on_or_before</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span> <span class="n">on_or_after</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span> <span class="n">between</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span> <span class="n">returning</span><span class="o">=</span><span class="s1">&#39;binary_flag&#39;</span><span class="p">,</span> <span class="n">date_format</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span> <span class="n">find_first_match_in_period</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span> <span class="n">find_last_match_in_period</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span> <span class="n">return_expectations</span><span class="o">=</span><span class="kc">None</span><span class="p">)</span></code>

<a href="#cohortextractor.patients.with_tpp_vaccination_record" class="headerlink" title="Permanent link">🔗</a></h4>


    <div class="doc doc-contents first">

        <p>Identify patients with a vaccination record for a target disease within the <abbr title="The company behind the SystmOne EHR">TPP</abbr> vaccination record</p>
<p>Vaccinations can be recorded via a Vaccination Record or via prescription of a vaccine i.e a product code.</p>


<p><span class="doc-section-title">Parameters:</span></p>
    <table>
      <thead>
        <tr>
          <th>Name</th>
          <th>Type</th>
          <th>Description</th>
          <th>Default</th>
        </tr>
      </thead>
      <tbody>
          <tr class="doc-section-item">
            <td>
                <code>target_disease_matches</code>
            </td>
            <td>
            </td>
            <td>
              <div class="doc-md-description">
                <p>the target disease as a string</p>
              </div>
            </td>
            <td>
                  <code>None</code>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>product_name_matches</code>
            </td>
            <td>
            </td>
            <td>
              <div class="doc-md-description">
                <p>the product name as a string</p>
              </div>
            </td>
            <td>
                  <code>None</code>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>on_or_before</code>
            </td>
            <td>
            </td>
            <td>
              <div class="doc-md-description">
                <p>date of interest as a string with the format <code>YYYY-MM-DD</code>. Filters results to
on or before the given date.</p>
              </div>
            </td>
            <td>
                  <code>None</code>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>on_or_after</code>
            </td>
            <td>
            </td>
            <td>
              <div class="doc-md-description">
                <p>date of interest as a string with the format <code>YYYY-MM-DD</code>. Filters results to
on or after the given date.</p>
              </div>
            </td>
            <td>
                  <code>None</code>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>between</code>
            </td>
            <td>
            </td>
            <td>
              <div class="doc-md-description">
                <p>two dates of interest as a list with each date as a string with the format <code>YYYY-MM-DD</code>.
Filters results to between the two dates provided (inclusive).
The two dates must be in chronological order.</p>
              </div>
            </td>
            <td>
                  <code>None</code>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>returning</code>
            </td>
            <td>
            </td>
            <td>
              <div class="doc-md-description">
                <p>string indicating value to be returned. Options are:</p>
<ul>
<li><code>binary_flag</code>: indicates if they have had the vaccination or not</li>
<li><code>date</code>: date of vaccination</li>
</ul>
              </div>
            </td>
            <td>
                  <code>&#39;binary_flag&#39;</code>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>date_format</code>
            </td>
            <td>
            </td>
            <td>
              <div class="doc-md-description">
                <p>a string detailing the format of the dates to be returned. It can be <code>YYYY-MM-DD</code>,
<code>YYYY-MM</code> or <code>YYYY</code> and wherever possible the least disclosive data should be returned. i.e returning
only year is less disclosive than a date with day, month and year.</p>
              </div>
            </td>
            <td>
                  <code>None</code>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>find_first_match_in_period</code>
            </td>
            <td>
            </td>
            <td>
              <div class="doc-md-description">
                <p>a boolean that indicates if the data returned is first indication of vaccination
if there are multiple matches within the time period</p>
              </div>
            </td>
            <td>
                  <code>None</code>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>find_last_match_in_period</code>
            </td>
            <td>
            </td>
            <td>
              <div class="doc-md-description">
                <p>a boolean that indicates if the data returned is last indication of vaccination
if there are multiple matches within the time period</p>
              </div>
            </td>
            <td>
                  <code>None</code>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>return_expectations</code>
            </td>
            <td>
            </td>
            <td>
              <div class="doc-md-description">
                <p>a dictionary defining the incidence and distribution of expected value
within the population in question.</p>
              </div>
            </td>
            <td>
                  <code>None</code>
            </td>
          </tr>
      </tbody>
    </table>


    <p><span class="doc-section-title">Returns:</span></p>
    <table>
      <thead>
        <tr>
<th>Name</th>          <th>Type</th>
          <th>Description</th>
        </tr>
      </thead>
      <tbody>
          <tr class="doc-section-item">
<td><code>list</code></td>            <td>
            </td>
            <td>
              <div class="doc-md-description">
                <p>of integers of <code>1</code> or <code>0</code> if <code>returning</code> argument is set to <code>binary_flag</code>;
list of strings with a date format returned if <code>returning</code> argument is set to <code>date</code></p>
              </div>
            </td>
          </tr>
      </tbody>
    </table>
        <p>Example:</p>
<div class="highlight"><pre><span></span><code>A variable called `flu_vaccine` is created that returns the date of vaccination for
any patients in the GP dataset between 2 dates.

    flu_vaccine=patients.with_tpp_vaccination_record(
        target_disease_matches=&quot;influenza&quot;,
        between=[&quot;2019-09-01&quot;, &quot;2020-04-01&quot;],
        returning=&quot;date&quot;,
        date_format=&quot;YYYY-MM-DD&quot;,
        find_first_match_in_period=True,
        return_expectations={
            date&quot;: {&quot;earliest&quot;: &quot;2019-09-01&quot;, &quot;latest&quot;: &quot;2020-03-29&quot;}
        }
    ),
</code></pre></div>


    </div>

</div><p>&nbsp;</p>


<div class="doc doc-object doc-function">


<h4 id="cohortextractor.patients.household_as_of" class="doc doc-heading">
            <code class="highlight language-python"><span class="n">household_as_of</span><span class="p">(</span><span class="n">reference_date</span><span class="p">,</span> <span class="n">returning</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span> <span class="n">return_expectations</span><span class="o">=</span><span class="kc">None</span><span class="p">)</span></code>

<a href="#cohortextractor.patients.household_as_of" class="headerlink" title="Permanent link">🔗</a></h4>


    <div class="doc doc-contents first">

        <p>Return information about the household to which the patient belonged as of
the reference date. This is inferred from address data using an algorithm
developed by <abbr title="The company behind the SystmOne EHR">TPP</abbr> (to be documented soon) so the results are not 100%
reliable but are apparently pretty good.</p>


<p><span class="doc-section-title">Parameters:</span></p>
    <table>
      <thead>
        <tr>
          <th>Name</th>
          <th>Type</th>
          <th>Description</th>
          <th>Default</th>
        </tr>
      </thead>
      <tbody>
          <tr class="doc-section-item">
            <td>
                <code>reference_date</code>
            </td>
            <td>
            </td>
            <td>
              <div class="doc-md-description">
                <p>date of interest as a string with the format <code>YYYY-MM-DD</code>. Filters results to a particular set date.</p>
              </div>
            </td>
            <td>
                <em>required</em>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>returning</code>
            </td>
            <td>
            </td>
            <td>
              <div class="doc-md-description">
                <p>string indicating value to be returned. Options are:</p>
<ul>
<li><code>pseudo_id</code>: An integer identifier for the household which has no
   meaning other than to identify individual members of the same
   household (0 if no household information available)</li>
<li><code>household_size</code>: the number of individuals in the household (0
   if no household information available)</li>
<li><code>is_prison</code>: Boolean indicating whether household is a prison.
   See https://github.com/opensafely/cohort-extractor/issues/271#issuecomment-679069981
   for details of how this is determined</li>
<li><code>has_members_in_other_ehr_systems</code>: Boolean indicating whether
   some household members are registered with GPs using a different
   <abbr title="Electronic Health Record">EHR</abbr> system, meaning that our coverage of the household is
   incomplete.</li>
<li><code>percentage_of_members_with_data_in_this_backend</code>: Integer giving
   the (estimated) percentage of household members where we have
   <abbr title="Electronic Health Record">EHR</abbr> data available in this <abbr title="an individual clinical database that a data provider makes accessible via the OpenSAFELY platform.">backend</abbr> (i.e. not in other systems as
   above).</li>
<li><code>msoa</code>: Returns the MSOA (Middle Super Output Area) in which the
   household is situated</li>
</ul>
              </div>
            </td>
            <td>
                  <code>None</code>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>return_expectations</code>
            </td>
            <td>
            </td>
            <td>
              <div class="doc-md-description">
                <p>a dictionary defining the incidence and distribution of expected value within the population in question.</p>
              </div>
            </td>
            <td>
                  <code>None</code>
            </td>
          </tr>
      </tbody>
    </table>


    <p><span class="doc-section-title">Returns:</span></p>
    <table>
      <thead>
        <tr>
<th>Name</th>          <th>Type</th>
          <th>Description</th>
        </tr>
      </thead>
      <tbody>
          <tr class="doc-section-item">
<td><code>list</code></td>            <td>
            </td>
            <td>
              <div class="doc-md-description">
                <p>of integers if <code>returning</code> argument is set to <code>pseudo_id</code>, <code>household_size</code> or</p>
              </div>
            </td>
          </tr>
          <tr class="doc-section-item">
<td></td>            <td>
            </td>
            <td>
              <div class="doc-md-description">
                <p><code>percentage_of_members_with_data_in_this_backend</code>. a list of <code>1</code> or <code>0</code> is <code>returning</code> is set to</p>
              </div>
            </td>
          </tr>
          <tr class="doc-section-item">
<td></td>            <td>
            </td>
            <td>
              <div class="doc-md-description">
                <p><code>is_prison</code> or <code>has_members_in_other_ehr_systems</code></p>
              </div>
            </td>
          </tr>
          <tr class="doc-section-item">
<td><code>Examples</code></td>            <td>
            </td>
            <td>
              <div class="doc-md-description">
                <p>household_id=patients.household_as_of(
    "2020-02-01", returning="pseudo_id"
)</p>
<p>household_size=patients.household_as_of(
    "2020-02-01", returning="household_size"
),</p>
              </div>
            </td>
          </tr>
      </tbody>
    </table>


    </div>

</div><p>&nbsp;</p>


<div class="doc doc-object doc-function">


<h4 id="cohortextractor.patients.with_these_decision_support_values" class="doc doc-heading">
            <code class="highlight language-python"><span class="n">with_these_decision_support_values</span><span class="p">(</span><span class="n">algorithm</span><span class="p">,</span> <span class="n">on_or_before</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span> <span class="n">on_or_after</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span> <span class="n">between</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span> <span class="n">find_first_match_in_period</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span> <span class="n">find_last_match_in_period</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span> <span class="n">returning</span><span class="o">=</span><span class="s1">&#39;numeric_value&#39;</span><span class="p">,</span> <span class="n">include_date_of_match</span><span class="o">=</span><span class="kc">False</span><span class="p">,</span> <span class="n">date_format</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span> <span class="n">ignore_missing_values</span><span class="o">=</span><span class="kc">False</span><span class="p">,</span> <span class="n">return_expectations</span><span class="o">=</span><span class="kc">None</span><span class="p">)</span></code>

<a href="#cohortextractor.patients.with_these_decision_support_values" class="headerlink" title="Permanent link">🔗</a></h4>


    <div class="doc doc-contents first">

        <p>Returns values computed by the given decision support algorithm.</p>


<p><span class="doc-section-title">Parameters:</span></p>
    <table>
      <thead>
        <tr>
          <th>Name</th>
          <th>Type</th>
          <th>Description</th>
          <th>Default</th>
        </tr>
      </thead>
      <tbody>
          <tr class="doc-section-item">
            <td>
                <code>algorithm</code>
            </td>
            <td>
            </td>
            <td>
              <div class="doc-md-description">
                <p>a string indicating the decision support algorithm. Currently, the only option is <code>electronic_frailty_index</code> for the electronic frailty index algorithm.</p>
              </div>
            </td>
            <td>
                <em>required</em>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>on_or_before</code>
            </td>
            <td>
            </td>
            <td>
              <div class="doc-md-description">
                <p>the date of interest as a string with the format <code>YYYY-MM-DD</code>. Filters matches to on or before the given date.</p>
              </div>
            </td>
            <td>
                  <code>None</code>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>on_or_after</code>
            </td>
            <td>
            </td>
            <td>
              <div class="doc-md-description">
                <p>the date of interest as a string with the format <code>YYYY-MM-DD</code>. Filters matches to on or after the given date.</p>
              </div>
            </td>
            <td>
                  <code>None</code>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>between</code>
            </td>
            <td>
            </td>
            <td>
              <div class="doc-md-description">
                <p>two dates of interest as a list with each date as a string with the format <code>YYYY-MM-DD</code>. Filters matches to between the two dates (inclusive).
The two dates must be in chronological order.</p>
              </div>
            </td>
            <td>
                  <code>None</code>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>find_first_match_in_period</code>
            </td>
            <td>
            </td>
            <td>
              <div class="doc-md-description">
                <p>a boolean indicating if values should be based on the first match in the period.</p>
              </div>
            </td>
            <td>
                  <code>None</code>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>find_last_match_in_period</code>
            </td>
            <td>
            </td>
            <td>
              <div class="doc-md-description">
                <p>a boolean indicating if values should be based on the last match in the period. This is the default behaviour.</p>
              </div>
            </td>
            <td>
                  <code>None</code>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>returning</code>
            </td>
            <td>
            </td>
            <td>
              <div class="doc-md-description">
                <p>a string indicating the values to return. The options are:
* <code>binary_flag</code>
* <code>date</code>
* <code>number_of_matches_in_period</code>
* <code>numeric_value</code> The default value.</p>
              </div>
            </td>
            <td>
                  <code>&#39;numeric_value&#39;</code>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>include_date_of_match</code>
            </td>
            <td>
            </td>
            <td>
              <div class="doc-md-description">
                <p>a boolean indicating if an extra column containing the date of the match should be returned.</p>
              </div>
            </td>
            <td>
                  <code>False</code>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>date_format</code>
            </td>
            <td>
            </td>
            <td>
              <div class="doc-md-description">
                <p>a string indicating the format of any dates included in the values. It can be <code>YYYY-MM-DD</code>, <code>YYYY-MM</code>, or <code>YYYY</code>. Wherever possible the least disclosive dates should be returned i.e returning dates with year and month is less disclosive than returning dates with year, month, and day. Only used if <code>include_date_of_match=True</code>.</p>
              </div>
            </td>
            <td>
                  <code>None</code>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>ignore_missing_values</code>
            </td>
            <td>
            </td>
            <td>
              <div class="doc-md-description">
                <p>a boolean indicating if matches where the value is missing or zero should be ignored. We are unable to distinguish between null values (missing) and zeros due to limitations in how the data are recorded by <abbr title="The company behind the SystmOne EHR">TPP</abbr>.</p>
              </div>
            </td>
            <td>
                  <code>False</code>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>return_expectations</code>
            </td>
            <td>
            </td>
            <td>
              <div class="doc-md-description">
                <p>as described elsewhere.</p>
              </div>
            </td>
            <td>
                  <code>None</code>
            </td>
          </tr>
      </tbody>
    </table>


    </div>

</div><p>&nbsp;</p>

## ICNARC
!!! warning
    ICNARC data can only be used in collaboration with ICNARC researchers who must be involved in working on the study and writing it up.
    Please contact your co-pilot, or <team@opensafely.org> if you have any questions.

!!! warning
    Data from ICNARC were last imported on 21-Jan-2021, with no further imports currently planned. Alternative data on ICU admission can be gleaned from SUS (i.e. returning=days_in_critical_care).

These variables are derived from the Intensive Care National Audit and Research Centre Case-Mix Programme (ICNARC-CMP), which collects information on ICU admissions across England.
For more information, see the [ICNARC data section](../data-sources/icnarc.md).
&nbsp;


<div class="doc doc-object doc-function">


<h4 id="cohortextractor.patients.admitted_to_icu" class="doc doc-heading">
            <code class="highlight language-python"><span class="n">admitted_to_icu</span><span class="p">(</span><span class="n">on_or_after</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span> <span class="n">on_or_before</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span> <span class="n">between</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span> <span class="n">find_first_match_in_period</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span> <span class="n">find_last_match_in_period</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span> <span class="n">returning</span><span class="o">=</span><span class="s1">&#39;binary_flag&#39;</span><span class="p">,</span> <span class="n">date_format</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span> <span class="n">return_expectations</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span> <span class="n">include_month</span><span class="o">=</span><span class="kc">False</span><span class="p">,</span> <span class="n">include_day</span><span class="o">=</span><span class="kc">False</span><span class="p">)</span></code>

<a href="#cohortextractor.patients.admitted_to_icu" class="headerlink" title="Permanent link">🔗</a></h4>


    <div class="doc doc-contents first">

        <p>Return information about being admitted to ICU.</p>


<p><span class="doc-section-title">Parameters:</span></p>
    <table>
      <thead>
        <tr>
          <th>Name</th>
          <th>Type</th>
          <th>Description</th>
          <th>Default</th>
        </tr>
      </thead>
      <tbody>
          <tr class="doc-section-item">
            <td>
                <code>on_or_before</code>
            </td>
            <td>
            </td>
            <td>
              <div class="doc-md-description">
                <p>date of interest as a string with the format <code>YYYY-MM-DD</code>. Filters results
on or before the given date.</p>
              </div>
            </td>
            <td>
                  <code>None</code>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>on_or_after</code>
            </td>
            <td>
            </td>
            <td>
              <div class="doc-md-description">
                <p>date of interest as a string with the format <code>YYYY-MM-DD</code>. Filters results
on or after the given date.</p>
              </div>
            </td>
            <td>
                  <code>None</code>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>between</code>
            </td>
            <td>
            </td>
            <td>
              <div class="doc-md-description">
                <p>two dates of interest as a list with each date as a string with the format <code>YYYY-MM-DD</code>.
Filters results between the two dates provided (inclusive).
The two dates must be in chronological order.</p>
              </div>
            </td>
            <td>
                  <code>None</code>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>find_first_match_in_period</code>
            </td>
            <td>
            </td>
            <td>
              <div class="doc-md-description">
                <p>a boolean that indicates if the data returned is first admission to icu if
there are multiple admissions within the time period</p>
              </div>
            </td>
            <td>
                  <code>None</code>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>find_last_match_in_period</code>
            </td>
            <td>
            </td>
            <td>
              <div class="doc-md-description">
                <p>a boolean that indicates if the data returned is last admission to icu if
there are multiple admissions within the time period</p>
              </div>
            </td>
            <td>
                  <code>None</code>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>returning</code>
            </td>
            <td>
            </td>
            <td>
              <div class="doc-md-description">
                <p>string indicating value to be returned. Options are:</p>
<ul>
<li><code>binary_flag</code>: Whether patient attended ICU</li>
<li><code>date_admitted</code>: Date patient arrived in ICU</li>
<li><code>had_respiratory_support</code>: Whether patient received any form of respiratory support</li>
<li><code>had_basic_respiratory_support</code>: Whether patient received "basic" respiratory support</li>
<li><code>had_advanced_respiratory_support</code>: Whether patient received "advanced" respiratory support</li>
</ul>
<p>(Note that the terms "basic" and "advanced" are derived from the underlying <abbr title="Intensive Care National Audit and Research Centre">ICNARC</abbr> data.)</p>
              </div>
            </td>
            <td>
                  <code>&#39;binary_flag&#39;</code>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>date_format</code>
            </td>
            <td>
            </td>
            <td>
              <div class="doc-md-description">
                <p>a string detailing the format of the dates to be returned. It can be <code>YYYY-MM-DD</code>,
<code>YYYY-MM</code> or <code>YYYY</code> and wherever possible the least disclosive data should be returned. i.e returning
only year is less disclosive than a date with day, month and year. Only used if
<code>returning</code> is <code>binary_flag</code></p>
              </div>
            </td>
            <td>
                  <code>None</code>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>return_expectations</code>
            </td>
            <td>
            </td>
            <td>
              <div class="doc-md-description">
                <p>a dictionary defining the incidence and distribution of expected value
within the population in question. This is a 2-item key-value dictionary of <code>date</code> and <code>rate</code>.</p>
              </div>
            </td>
            <td>
                  <code>None</code>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>include_month</code>
            </td>
            <td>
            </td>
            <td>
              <div class="doc-md-description">
                <p>a boolean indicating if day should be included in addition to year (deprecated: use
<code>date_format</code> instead).</p>
              </div>
            </td>
            <td>
                  <code>False</code>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>include_day</code>
            </td>
            <td>
            </td>
            <td>
              <div class="doc-md-description">
                <p>a boolean indicating if day should be included in addition to year and
month (deprecated: use <code>date_format</code> instead).</p>
              </div>
            </td>
            <td>
                  <code>False</code>
            </td>
          </tr>
      </tbody>
    </table>


    <p><span class="doc-section-title">Returns:</span></p>
    <table>
      <thead>
        <tr>
<th>Name</th>          <th>Type</th>
          <th>Description</th>
        </tr>
      </thead>
      <tbody>
          <tr class="doc-section-item">
<td><code>list</code></td>            <td>
            </td>
            <td>
              <div class="doc-md-description">
                <p>of integers of <code>1</code> or <code>0</code> if <code>returning</code> argument is set to <code>binary_flag</code>, <code>had_respiratory_support</code>,</p>
              </div>
            </td>
          </tr>
          <tr class="doc-section-item">
<td></td>            <td>
            </td>
            <td>
              <div class="doc-md-description">
                <p><code>had_basic_respiratory_support</code> or <code>had_advanced_respiratory_support</code>; list of strings with a date format</p>
              </div>
            </td>
          </tr>
          <tr class="doc-section-item">
<td></td>            <td>
            </td>
            <td>
              <div class="doc-md-description">
                <p>returned if <code>returning</code> argument is set to <code>date_admitted</code></p>
              </div>
            </td>
          </tr>
      </tbody>
    </table>
        <p>Example:</p>
<div class="highlight"><pre><span></span><code>This returns two variables &amp;mdash; one called `icu_date_admitted` and another `had_resp_support`:

    has_resp_support=patients.admitted_to_icu(
        on_or_after=&quot;2020-02-01&quot;,
        find_first_match_in_period=True,
        returning=&quot;had_respiratory_support&quot;,
        return_expectations={
                &quot;date&quot;: {&quot;earliest&quot; : &quot;2020-02-01&quot;},
                &quot;rate&quot; : &quot;exponential_increase&quot;
        },
    ),

    icu_date_admitted=patients.admitted_to_icu(
        on_or_after=&quot;2020-02-01&quot;,
        find_first_match_in_period=True,
        returning=&quot;date_admitted&quot;,
        date_format=&quot;YYYY-MM-DD&quot;,
        return_expectations={
            &quot;date&quot;: {&quot;earliest&quot; : &quot;2020-02-01&quot;},
            &quot;rate&quot; : &quot;exponential_increase&quot;
       },
    ),
</code></pre></div>


    </div>

</div><p>&nbsp;</p>

## SGSS
These variables are derived from Second Generation Surveillance System (SGSS) data which captures routine laboratory surveillance data on infectious diseases across England.
For more information, see the [SGSS data section](../data-sources/sgsscovid.md).
&nbsp;


<div class="doc doc-object doc-function">


<h4 id="cohortextractor.patients.with_test_result_in_sgss" class="doc doc-heading">
            <code class="highlight language-python"><span class="n">with_test_result_in_sgss</span><span class="p">(</span><span class="n">pathogen</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span> <span class="n">test_result</span><span class="o">=</span><span class="s1">&#39;any&#39;</span><span class="p">,</span> <span class="n">on_or_before</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span> <span class="n">on_or_after</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span> <span class="n">between</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span> <span class="n">find_first_match_in_period</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span> <span class="n">find_last_match_in_period</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span> <span class="n">restrict_to_earliest_specimen_date</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span> <span class="n">returning</span><span class="o">=</span><span class="s1">&#39;binary_flag&#39;</span><span class="p">,</span> <span class="n">date_format</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span> <span class="n">return_expectations</span><span class="o">=</span><span class="kc">None</span><span class="p">)</span></code>

<a href="#cohortextractor.patients.with_test_result_in_sgss" class="headerlink" title="Permanent link">🔗</a></h4>


    <div class="doc doc-contents first">

        <p>Finds COVID lab test results recorded in <abbr title="Second Generation Surveillance System: an application that stores and manages data on laboratory isolates and notifications. PHE's preferred method for capturing routine laboratory surveillance data on infectious diseases and antimicrobial resistance from laboratories across England">SGSS</abbr> (Second Generation
Surveillance System).</p>
<p>Please note that all dates used here are "specimen dates" (i.e. the date
the specimen was taken), rather than the date the lab result was obtained.</p>
<p>It's important to note that data is supplied in two separate datasets: an
"Earliest Specimen" <abbr title="A tabular data structure with one row per patient and one column per variable.">dataset</abbr> and an "All Tests" <abbr title="A tabular data structure with one row per patient and one column per variable.">dataset</abbr>.</p>
<h6 id="cohortextractor.patients.with_test_result_in_sgss--earliest-specimen-dataset">Earliest Specimen Dataset<a class="headerlink" href="#cohortextractor.patients.with_test_result_in_sgss--earliest-specimen-dataset" title="Permanent link">🔗</a></h6>
<p>Where a patient has multiple positive tests, <abbr title="Second Generation Surveillance System: an application that stores and manages data on laboratory isolates and notifications. PHE's preferred method for capturing routine laboratory surveillance data on infectious diseases and antimicrobial resistance from laboratories across England">SGSS</abbr> groups these into
"episodes" (referred to as "Organism-Patient-Illness-Episodes"). Each
pathogen has a maximum episode duration (usually 2 weeks) and unless
positive tests are separated by longer than this period they are assumed to
be the same episode of illness.  The specimen date recorded is the
<em>earliest</em> positive specimen within the episode.</p>
<p>For SARS-CoV-2 the episode length has been set to infinity, meaning that
once a patient has tested positive every positive test will be part of the
same episode and record the same specimen date.</p>
<p>This means that using <code>find_last_match_in_period</code> is pointless when
querying for positive results as only one date will ever be recorded and it
will be the earliest.</p>
<p>Our original assumption, though the documentation didn't state either way,
is that every negative result would be treated as unique. However this does
not appear to be the case as though some patients do have multiple negative
tests in this <abbr title="A tabular data structure with one row per patient and one column per variable.">dataset</abbr>, the number is far too small to be realistic.</p>
<p>Information about the SARS-CoV-2 episode length was via email from someone
at the National Infection Service:</p>
<div class="highlight"><pre><span></span><code>The COVID-19 episode length in SGSS was set to indefinite, so all
COVID-19 records from a single patient will be classified as one
episode. This may change, but is set as it is due to limited
information around re-infection and virus clearance.
</code></pre></div>
<h6 id="cohortextractor.patients.with_test_result_in_sgss--all-tests-dataset">All Tests Dataset<a class="headerlink" href="#cohortextractor.patients.with_test_result_in_sgss--all-tests-dataset" title="Permanent link">🔗</a></h6>
<p>This <abbr title="A tabular data structure with one row per patient and one column per variable.">dataset</abbr> is not subject to the same restriction as above and we expect
each individual test result (postive or negative) to appear in this
regardless of whether they are considered as within the same infection
episode. In an ideal world we could use just this <abbr title="A tabular data structure with one row per patient and one column per variable.">dataset</abbr>, but there are
some fields we need (e.g. Case Category) which are only supplied on the
"earliest specimen" <abbr title="A tabular data structure with one row per patient and one column per variable.">dataset</abbr>.</p>
<h6 id="cohortextractor.patients.with_test_result_in_sgss--s-gene-target-failure">S-Gene Target Failure<a class="headerlink" href="#cohortextractor.patients.with_test_result_in_sgss--s-gene-target-failure" title="Permanent link">🔗</a></h6>
<p>Using the <code>returning="s_gene_target_failure"</code> option provides additional
output from PCR tests results which can be used as a proxy for the presence
of certain Variants of Concern.</p>
<p>Possible values are "", "0", "1", "9"</p>
<p>Definitions (from email from <abbr title="Public Health England">PHE</abbr>)</p>
<div class="highlight"><pre><span></span><code>1: Isolate with confirmed SGTF
Undetectable S gene; CT value (CH3) =0
Detectable ORF1ab gene; CT value (CH2) &lt;=30 and &gt;0
Detectable N gene; CT value (CH1) &lt;=30 and &gt;0

0: S gene detected
Detectable S gene (CH3&gt;0)
Detectable y ORF1ab CT value (CH1) &lt;=30 and &gt;0
Detectable N gene CT value (CH2) &lt;=30 and &gt;0

9: Cannot be classified

Null are where the target is not S Gene. I think LFTs are currently
also coming across as 9 so will need to review those to null as well as
clearly this is a PCR only variable.
</code></pre></div>
<h6 id="cohortextractor.patients.with_test_result_in_sgss--case-category-type-of-test-used">Case Category (type of test used)<a class="headerlink" href="#cohortextractor.patients.with_test_result_in_sgss--case-category-type-of-test-used" title="Permanent link">🔗</a></h6>
<p>Using the <code>returning="case_category"</code> option (only available on positive,
earliest specimen date results) reports whether the test was a Lateral Flow
or PCR test. Possible values are:</p>
<div class="highlight"><pre><span></span><code>&quot;LFT_Only&quot;, &quot;PCR_Only&quot;, &quot;LFT_WithPCR&quot;
</code></pre></div>
<h6 id="cohortextractor.patients.with_test_result_in_sgss--variant">Variant<a class="headerlink" href="#cohortextractor.patients.with_test_result_in_sgss--variant" title="Permanent link">🔗</a></h6>
<p>The <code>returning="variant"</code> option (only available in the "All Tests" data)
returns details on specific SARS-CoV-2 variants detected. Possible values
include, but are not limited to:</p>
<div class="highlight"><pre><span></span><code>B.1.617.2
VOC-21JAN-02
VUI-21FEB-04
P.1
E484K
B.1.1.7+E484K
No VOC detected
Sequencing Failed
Undetermined
Undetermined + e484k
</code></pre></div>
<p>The <code>returning="variant_detection_method"</code> options returns possible values:</p>
<div class="highlight"><pre><span></span><code>&quot;Reflex Assay&quot; and &quot;Private Lab Sequencing&quot;
</code></pre></div>
<h6 id="cohortextractor.patients.with_test_result_in_sgss--symptomatic">Symptomatic<a class="headerlink" href="#cohortextractor.patients.with_test_result_in_sgss--symptomatic" title="Permanent link">🔗</a></h6>
<p>The <code>returning="symptomatic"</code> option (only available in the "All Tests" data)
returns details on whether patients are symptomatic of SARS-CoV-2 or not. This
option is available regardless of the test result outcome.</p>
<p>Possible values are "", "Y", "N".</p>
<h6 id="cohortextractor.patients.with_test_result_in_sgss--number-of-tests">Number of Tests<a class="headerlink" href="#cohortextractor.patients.with_test_result_in_sgss--number-of-tests" title="Permanent link">🔗</a></h6>
<p>The <code>returning="number_of_matches_in_period"</code> option (only available in the "All Tests" data)
returns a count of the number of tests a patient has had in the defined time period.</p>
<p>It is used with <code>test_result</code> which must be set as "positive", "negative" or "any".
<code>returning="number_of_matches_in_period"</code> can therefore be used to return the number of
positive, negative or all tests.</p>
<p>For more detail on <abbr title="Second Generation Surveillance System: an application that stores and manages data on laboratory isolates and notifications. PHE's preferred method for capturing routine laboratory surveillance data on infectious diseases and antimicrobial resistance from laboratories across England">SGSS</abbr> in general see <a href="https://assets.publishing.service.gov.uk/government/uploads/system/uploads/attachment_data/file/739854/PHE_Laboratory_Reporting_Guidelines.pdf">PHE_Laboratory_Reporting_Guidelines.pdf</a></p>


<p><span class="doc-section-title">Parameters:</span></p>
    <table>
      <thead>
        <tr>
          <th>Name</th>
          <th>Type</th>
          <th>Description</th>
          <th>Default</th>
        </tr>
      </thead>
      <tbody>
          <tr class="doc-section-item">
            <td>
                <code>pathogen</code>
            </td>
            <td>
            </td>
            <td>
              <div class="doc-md-description">
                <p>pathogen we are interested in. Only SARS-CoV-2 results are
included in our data extract so this will throw an error if the
specified pathogen is anything other than "SARS-CoV-2".</p>
              </div>
            </td>
            <td>
                  <code>None</code>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>test_result</code>
            </td>
            <td>
            </td>
            <td>
              <div class="doc-md-description">
                <p>must be one of "positive", "negative" or "any"</p>
              </div>
            </td>
            <td>
                  <code>&#39;any&#39;</code>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>on_or_before</code>
            </td>
            <td>
            </td>
            <td>
              <div class="doc-md-description">
                <p>date of interest as a string with the format
<code>YYYY-MM-DD</code>. Filters results to on or before the given date. The
default value is <code>None</code>.</p>
              </div>
            </td>
            <td>
                  <code>None</code>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>on_or_after</code>
            </td>
            <td>
            </td>
            <td>
              <div class="doc-md-description">
                <p>date of interest as a string with the format <code>YYYY-MM-DD</code>.
Filters results to on or after the given date.</p>
              </div>
            </td>
            <td>
                  <code>None</code>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>between</code>
            </td>
            <td>
            </td>
            <td>
              <div class="doc-md-description">
                <p>two dates of interest as a list with each date as a string
with the format <code>YYYY-MM-DD</code>.  Filters results to between the two
dates provided. The two dates must be in chronological order.</p>
              </div>
            </td>
            <td>
                  <code>None</code>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>find_first_match_in_period</code>
            </td>
            <td>
            </td>
            <td>
              <div class="doc-md-description">
                <p>a boolean that indicates if the data
returned is first event if there are multiple matches within the
time period</p>
              </div>
            </td>
            <td>
                  <code>None</code>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>find_last_match_in_period</code>
            </td>
            <td>
            </td>
            <td>
              <div class="doc-md-description">
                <p>a boolean that indicates if the data
returned is last event if there are multiple matches within the
time period</p>
              </div>
            </td>
            <td>
                  <code>None</code>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>restrict_to_earliest_specimen_date</code>
            </td>
            <td>
            </td>
            <td>
              <div class="doc-md-description">
                <p>a boolean indicating whether to use
the "earliest specimen" or "all tests" <abbr title="A tabular data structure with one row per patient and one column per variable.">dataset</abbr> (see above). True by
default, meaning that the "earliest specimen" <abbr title="A tabular data structure with one row per patient and one column per variable.">dataset</abbr> is used.</p>
              </div>
            </td>
            <td>
                  <code>True</code>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>returning</code>
            </td>
            <td>
            </td>
            <td>
              <div class="doc-md-description">
                <p>string indicating value to be returned. Options are:</p>
<ul>
<li><code>binary_flag</code>: indicates if they have had the an event or not</li>
<li><code>date</code>: indicates date of event and used with either find_first_match_in_period or find_last_match_in_period</li>
<li><code>s_gene_target_failure</code>: returns the value of the SGTF field (see above)</li>
<li><code>case_category</code> (see above)</li>
<li><code>variant</code> (see above)</li>
<li><code>variant_detection_method</code> (see above)</li>
<li><code>symptomatic</code> (see above)</li>
<li><code>number_of_matches_in_period</code> (see above)</li>
</ul>
              </div>
            </td>
            <td>
                  <code>&#39;binary_flag&#39;</code>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>date_format</code>
            </td>
            <td>
            </td>
            <td>
              <div class="doc-md-description">
                <p>a string detailing the format of the dates to be returned.
It can be <code>YYYY-MM-DD</code>, <code>YYYY-MM</code> or <code>YYYY</code> and wherever possible
the least disclosive data should be returned. i.e returning only
year is less disclosive than a date with day, month and year.</p>
              </div>
            </td>
            <td>
                  <code>None</code>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>return_expectations</code>
            </td>
            <td>
            </td>
            <td>
              <div class="doc-md-description">
                <p>a dictionary defining the incidence and
distribution of expected value within the population in question.</p>
              </div>
            </td>
            <td>
                  <code>None</code>
            </td>
          </tr>
      </tbody>
    </table>


    <p><span class="doc-section-title">Returns:</span></p>
    <table>
      <thead>
        <tr>
<th>Name</th>          <th>Type</th>
          <th>Description</th>
        </tr>
      </thead>
      <tbody>
          <tr class="doc-section-item">
<td><code>list</code></td>            <td>
            </td>
            <td>
              <div class="doc-md-description">
                <p>of integers of <code>1</code> or <code>0</code> if <code>returning</code> argument is set to
<code>binary_flag</code>; list of strings with a date format returned if
<code>returning</code> argument is set to <code>date</code>;</p>
              </div>
            </td>
          </tr>
      </tbody>
    </table>
        <p>Example:</p>
<div class="highlight"><pre><span></span><code>Two variables are created. One called `first_tested_for_covid` is the
first date that a patient has a covid test never mind the result. The
second called `first_positive_test_date` is the first date that a
patient has a positive test result.

    first_tested_for_covid=patients.with_test_result_in_sgss(
        pathogen=&quot;SARS-CoV-2&quot;,
        test_result=&quot;any&quot;,
        on_or_after=&quot;2020-02-01&quot;,
        find_first_match_in_period=True,
        returning=&quot;date&quot;,
        date_format=&quot;YYYY-MM-DD&quot;,
        return_expectations={
            &quot;date&quot;: {&quot;earliest&quot; : &quot;2020-02-01&quot;},
            &quot;rate&quot; : &quot;exponential_increase&quot;
        },
    ),
    first_positive_test_date=patients.with_test_result_in_sgss(
        pathogen=&quot;SARS-CoV-2&quot;,
        test_result=&quot;positive&quot;,
        on_or_after=&quot;2020-02-01&quot;,
        find_first_match_in_period=True,
        returning=&quot;date&quot;,
        date_format=&quot;YYYY-MM-DD&quot;,
        return_expectations={
            &quot;date&quot;: {&quot;earliest&quot; : &quot;2020-02-01&quot;},
            &quot;rate&quot; : &quot;exponential_increase&quot;
        },
    ),
</code></pre></div>


    </div>

</div><p>&nbsp;</p>

## CPNS

These variables are derived from the COVID-19 Patient Notification System (CPNS), which collects info on all in-hospital covid-related deaths.
For more information, see the [CPNS data section](../data-sources/cpns.md).

!!! note
    CPNS is restricted to in-hospital covid-related deaths only. For covid-related deaths in any setting, ONS-registered deaths where cause of death matches [COVID-19 coding in ICD-10](https://www.who.int/standards/classifications/classification-of-diseases/emergency-use-icd-codes-for-covid-19-disease-outbreak) is generally more useful.
&nbsp;


<div class="doc doc-object doc-function">


<h4 id="cohortextractor.patients.with_death_recorded_in_cpns" class="doc doc-heading">
            <code class="highlight language-python"><span class="n">with_death_recorded_in_cpns</span><span class="p">(</span><span class="n">on_or_before</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span> <span class="n">on_or_after</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span> <span class="n">between</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span> <span class="n">returning</span><span class="o">=</span><span class="s1">&#39;binary_flag&#39;</span><span class="p">,</span> <span class="n">date_format</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span> <span class="n">include_month</span><span class="o">=</span><span class="kc">False</span><span class="p">,</span> <span class="n">include_day</span><span class="o">=</span><span class="kc">False</span><span class="p">,</span> <span class="n">return_expectations</span><span class="o">=</span><span class="kc">None</span><span class="p">)</span></code>

<a href="#cohortextractor.patients.with_death_recorded_in_cpns" class="headerlink" title="Permanent link">🔗</a></h4>


    <div class="doc doc-contents first">

        <p>Identify patients who with death registered in <abbr title="Covid-19 Patient Notification System - the route by which NHS England are informed of COVID-19-positive, deaths in hospital">CPNS</abbr> <abbr title="A tabular data structure with one row per patient and one column per variable.">dataset</abbr></p>


<p><span class="doc-section-title">Parameters:</span></p>
    <table>
      <thead>
        <tr>
          <th>Name</th>
          <th>Type</th>
          <th>Description</th>
          <th>Default</th>
        </tr>
      </thead>
      <tbody>
          <tr class="doc-section-item">
            <td>
                <code>on_or_before</code>
            </td>
            <td>
            </td>
            <td>
              <div class="doc-md-description">
                <p>date of interest as a string with the format <code>YYYY-MM-DD</code>. Filters results
on or before the given date.</p>
              </div>
            </td>
            <td>
                  <code>None</code>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>on_or_after</code>
            </td>
            <td>
            </td>
            <td>
              <div class="doc-md-description">
                <p>date of interest as a string with the format <code>YYYY-MM-DD</code>. Filters results
on or after the given date.</p>
              </div>
            </td>
            <td>
                  <code>None</code>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>between</code>
            </td>
            <td>
            </td>
            <td>
              <div class="doc-md-description">
                <p>two dates of interest as a list with each date as a string with the format <code>YYYY-MM-DD</code>.
Filters results to between the two dates provided (inclusive).
The two dates must be in chronological order.</p>
              </div>
            </td>
            <td>
                  <code>None</code>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>returning</code>
            </td>
            <td>
            </td>
            <td>
              <div class="doc-md-description">
                <p>string indicating value to be returned. Options are:</p>
<ul>
<li><code>date_of_death</code>: Date of death</li>
<li><code>binary_flag</code>: If they died or not</li>
</ul>
              </div>
            </td>
            <td>
                  <code>&#39;binary_flag&#39;</code>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>date_format</code>
            </td>
            <td>
            </td>
            <td>
              <div class="doc-md-description">
                <p>a string detailing the format of the dates to be returned. It can be <code>YYYY-MM-DD</code>,
<code>YYYY-MM</code> or <code>YYYY</code> and wherever possible the least disclosive data should be returned. i.e returning
only year is less disclosive than a date with day, month and year.</p>
              </div>
            </td>
            <td>
                  <code>None</code>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>include_month</code>
            </td>
            <td>
            </td>
            <td>
              <div class="doc-md-description">
                <p>a boolean indicating if day should be included in addition to year (deprecated: use
<code>date_format</code> instead).</p>
              </div>
            </td>
            <td>
                  <code>False</code>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>include_day</code>
            </td>
            <td>
            </td>
            <td>
              <div class="doc-md-description">
                <p>a boolean indicating if day should be included in addition to year and
month (deprecated: use <code>date_format</code> instead).</p>
              </div>
            </td>
            <td>
                  <code>False</code>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>return_expectations</code>
            </td>
            <td>
            </td>
            <td>
              <div class="doc-md-description">
                <p>a dictionary defining the incidence and distribution of expected value
within the population in question.</p>
              </div>
            </td>
            <td>
                  <code>None</code>
            </td>
          </tr>
      </tbody>
    </table>


    <p><span class="doc-section-title">Returns:</span></p>
    <table>
      <thead>
        <tr>
<th>Name</th>          <th>Type</th>
          <th>Description</th>
        </tr>
      </thead>
      <tbody>
          <tr class="doc-section-item">
<td><code>list</code></td>            <td>
            </td>
            <td>
              <div class="doc-md-description">
                <p>of integers of <code>1</code> or <code>0</code> if <code>returning</code> argument is set to <code>binary_flag</code>;
list of strings with a date format returned if <code>returning</code> argument is set to <code>date_of_death</code></p>
              </div>
            </td>
          </tr>
      </tbody>
    </table>
        <p>Example:</p>
<div class="highlight"><pre><span></span><code>A variable called `died_date_cpns` is created that returns the date of death for
any patients have died in the CPNS dataset.

    died_date_cpns=patients.with_death_recorded_in_cpns(
        on_or_after=&quot;2020-02-01&quot;,
        returning=&quot;date_of_death&quot;,
        include_month=True,
        include_day=True,
        return_expectations={
            &quot;date&quot;: {&quot;earliest&quot; : &quot;2020-02-01&quot;},
            &quot;rate&quot; : &quot;exponential_increase&quot;
        },
    ),
</code></pre></div>


    </div>

</div>

&nbsp;


## ONS deaths
These variables are derived from the Death Registry data provided by the Office for National Statistics.
For more information, see the [ONS deaths section](../data-sources/onsdeaths.md).
&nbsp;


<div class="doc doc-object doc-function">


<h4 id="cohortextractor.patients.died_from_any_cause" class="doc doc-heading">
            <code class="highlight language-python"><span class="n">died_from_any_cause</span><span class="p">(</span><span class="n">on_or_before</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span> <span class="n">on_or_after</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span> <span class="n">between</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span> <span class="n">returning</span><span class="o">=</span><span class="s1">&#39;binary_flag&#39;</span><span class="p">,</span> <span class="n">date_format</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span> <span class="n">include_month</span><span class="o">=</span><span class="kc">False</span><span class="p">,</span> <span class="n">include_day</span><span class="o">=</span><span class="kc">False</span><span class="p">,</span> <span class="n">return_expectations</span><span class="o">=</span><span class="kc">None</span><span class="p">)</span></code>

<a href="#cohortextractor.patients.died_from_any_cause" class="headerlink" title="Permanent link">🔗</a></h4>


    <div class="doc doc-contents first">

        <p>Identify patients who with <abbr title="Office for National Statistics - the UK's largest independent producer of official statistics and the recognised national statistical institute of the UK">ONS</abbr>-registered deaths</p>


<p><span class="doc-section-title">Parameters:</span></p>
    <table>
      <thead>
        <tr>
          <th>Name</th>
          <th>Type</th>
          <th>Description</th>
          <th>Default</th>
        </tr>
      </thead>
      <tbody>
          <tr class="doc-section-item">
            <td>
                <code>on_or_before</code>
            </td>
            <td>
            </td>
            <td>
              <div class="doc-md-description">
                <p>date of interest as a string with the format <code>YYYY-MM-DD</code>. Filters results
on or before the given date.</p>
              </div>
            </td>
            <td>
                  <code>None</code>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>on_or_after</code>
            </td>
            <td>
            </td>
            <td>
              <div class="doc-md-description">
                <p>date of interest as a string with the format <code>YYYY-MM-DD</code>. Filters results
on or after the given date.</p>
              </div>
            </td>
            <td>
                  <code>None</code>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>between</code>
            </td>
            <td>
            </td>
            <td>
              <div class="doc-md-description">
                <p>two dates of interest as a list with each date as a string with the format <code>YYYY-MM-DD</code>.
Filters results to between the two dates provided (inclusive).
The two dates must be in chronological order.</p>
              </div>
            </td>
            <td>
                  <code>None</code>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>returning</code>
            </td>
            <td>
            </td>
            <td>
              <div class="doc-md-description">
                <p>string indicating value to be returned. Options are:</p>
<ul>
<li><code>date_of_death</code>: Date of death</li>
<li><code>binary_flag</code>: If they died or not</li>
<li><code>underlying_cause_of_death</code>: The icd10 code corresponding to the underlying cause of death</li>
<li><code>place_of_death</code>: Place of death (currently only available for <abbr title="The company behind the SystmOne EHR">TPP</abbr>)
   Possible values are: "Care home", "Elsewhere", "Home", "Hospice", "Hospital", "Other communal establishment"</li>
</ul>
              </div>
            </td>
            <td>
                  <code>&#39;binary_flag&#39;</code>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>date_format</code>
            </td>
            <td>
            </td>
            <td>
              <div class="doc-md-description">
                <p>a string detailing the format of the dates to be returned. It can be <code>YYYY-MM-DD</code>,
<code>YYYY-MM</code> or <code>YYYY</code> and wherever possible the least disclosive data should be returned. i.e returning
only year is less disclosive than a date with day, month and year.</p>
              </div>
            </td>
            <td>
                  <code>None</code>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>include_month</code>
            </td>
            <td>
            </td>
            <td>
              <div class="doc-md-description">
                <p>a boolean indicating if day should be included in addition to year (deprecated: use
<code>date_format</code> instead).</p>
              </div>
            </td>
            <td>
                  <code>False</code>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>include_day</code>
            </td>
            <td>
            </td>
            <td>
              <div class="doc-md-description">
                <p>a boolean indicating if day should be included in addition to year and
month (deprecated: use <code>date_format</code> instead).</p>
              </div>
            </td>
            <td>
                  <code>False</code>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>return_expectations</code>
            </td>
            <td>
            </td>
            <td>
              <div class="doc-md-description">
                <p>a dictionary defining the incidence and distribution of expected value
within the population in question.</p>
              </div>
            </td>
            <td>
                  <code>None</code>
            </td>
          </tr>
      </tbody>
    </table>


    <p><span class="doc-section-title">Returns:</span></p>
    <table>
      <thead>
        <tr>
<th>Name</th>          <th>Type</th>
          <th>Description</th>
        </tr>
      </thead>
      <tbody>
          <tr class="doc-section-item">
<td><code>list</code></td>            <td>
            </td>
            <td>
              <div class="doc-md-description">
                <p>of integers of <code>1</code> or <code>0</code> if <code>returning</code> argument is set to <code>binary_flag</code>;
list of strings with a date format returned if <code>returning</code> argument is set to <code>date_of_death</code>
list of strings returned if <code>returning</code> argument is set to <code>underlying_cause_of_death</code> or <code>place_of_death</code></p>
              </div>
            </td>
          </tr>
      </tbody>
    </table>
        <p>Example:</p>
<div class="highlight"><pre><span></span><code>A variable called `died_any` is created that returns the date of death for
any patients that have died in the time period.

    died_any=patients.died_from_any_cause(
        on_or_after=&quot;2020-02-01&quot;,
        returning=&quot;date_of_death&quot;,
        date_format=&quot;YYYY-MM-DD&quot;,
        return_expectations={
            &quot;date&quot;: {&quot;earliest&quot; : &quot;2020-02-01&quot;},
            &quot;rate&quot; : &quot;exponential_increase&quot;
        },
    )
</code></pre></div>


    </div>

</div><p>&nbsp;</p>


<div class="doc doc-object doc-function">


<h4 id="cohortextractor.patients.with_these_codes_on_death_certificate" class="doc doc-heading">
            <code class="highlight language-python"><span class="n">with_these_codes_on_death_certificate</span><span class="p">(</span><span class="n">codelist</span><span class="p">,</span> <span class="n">on_or_before</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span> <span class="n">on_or_after</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span> <span class="n">between</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span> <span class="n">match_only_underlying_cause</span><span class="o">=</span><span class="kc">False</span><span class="p">,</span> <span class="n">returning</span><span class="o">=</span><span class="s1">&#39;binary_flag&#39;</span><span class="p">,</span> <span class="n">date_format</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span> <span class="n">include_month</span><span class="o">=</span><span class="kc">False</span><span class="p">,</span> <span class="n">include_day</span><span class="o">=</span><span class="kc">False</span><span class="p">,</span> <span class="n">return_expectations</span><span class="o">=</span><span class="kc">None</span><span class="p">)</span></code>

<a href="#cohortextractor.patients.with_these_codes_on_death_certificate" class="headerlink" title="Permanent link">🔗</a></h4>


    <div class="doc doc-contents first">

        <p>Identify patients with <abbr title="Office for National Statistics - the UK's largest independent producer of official statistics and the recognised national statistical institute of the UK">ONS</abbr>-registered death, where cause of death
matches the supplied icd10 <abbr title="a collection of clinical codes that define a particular condition, event or diagnosis.">codelist</abbr></p>


<p><span class="doc-section-title">Parameters:</span></p>
    <table>
      <thead>
        <tr>
          <th>Name</th>
          <th>Type</th>
          <th>Description</th>
          <th>Default</th>
        </tr>
      </thead>
      <tbody>
          <tr class="doc-section-item">
            <td>
                <code>codelist</code>
            </td>
            <td>
            </td>
            <td>
              <div class="doc-md-description">
                <p>a <abbr title="a collection of clinical codes that define a particular condition, event or diagnosis.">codelist</abbr> for requested value</p>
              </div>
            </td>
            <td>
                <em>required</em>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>on_or_before</code>
            </td>
            <td>
            </td>
            <td>
              <div class="doc-md-description">
                <p>date of interest as a string with the format <code>YYYY-MM-DD</code>. Filters results
on or before the given date.</p>
              </div>
            </td>
            <td>
                  <code>None</code>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>on_or_after</code>
            </td>
            <td>
            </td>
            <td>
              <div class="doc-md-description">
                <p>date of interest as a string with the format <code>YYYY-MM-DD</code>. Filters results
on or after the given date.</p>
              </div>
            </td>
            <td>
                  <code>None</code>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>between</code>
            </td>
            <td>
            </td>
            <td>
              <div class="doc-md-description">
                <p>two dates of interest as a list with each date as a string with the format <code>YYYY-MM-DD</code>.
Filters results between the two dates provided (inclusive). The two dates must be in chronological order.</p>
              </div>
            </td>
            <td>
                  <code>None</code>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>match_only_underlying_cause</code>
            </td>
            <td>
            </td>
            <td>
              <div class="doc-md-description">
                <p>boolean for indicating if filters results to only specified cause of death.</p>
              </div>
            </td>
            <td>
                  <code>False</code>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>returning</code>
            </td>
            <td>
            </td>
            <td>
              <div class="doc-md-description">
                <p>string indicating value to be returned. Options are:</p>
<ul>
<li><code>date_of_death</code>: Date of death</li>
<li><code>binary_flag</code>: If they died or not</li>
<li><code>underlying_cause_of_death</code>: The icd10 code corresponding to the underlying cause of death</li>
<li><code>place_of_death</code>: Place of death (currently only available for <abbr title="The company behind the SystmOne EHR">TPP</abbr>)
  Possible values are: "Care home", "Elsewhere", "Home", "Hospice", "Hospital", "Other communal establishment"</li>
</ul>
              </div>
            </td>
            <td>
                  <code>&#39;binary_flag&#39;</code>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>date_format</code>
            </td>
            <td>
            </td>
            <td>
              <div class="doc-md-description">
                <p>a string detailing the format of the dates to be returned. It can be <code>YYYY-MM-DD</code>,
<code>YYYY-MM</code> or <code>YYYY</code> and wherever possible the least disclosive data should be returned. i.e returning
only year is less disclosive than a date with day, month and year.</p>
              </div>
            </td>
            <td>
                  <code>None</code>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>include_month</code>
            </td>
            <td>
            </td>
            <td>
              <div class="doc-md-description">
                <p>a boolean indicating if day should be included in addition to year (deprecated: use
<code>date_format</code> instead).</p>
              </div>
            </td>
            <td>
                  <code>False</code>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>include_day</code>
            </td>
            <td>
            </td>
            <td>
              <div class="doc-md-description">
                <p>a boolean indicating if day should be included in addition to year and
month (deprecated: use <code>date_format</code> instead).</p>
              </div>
            </td>
            <td>
                  <code>False</code>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>return_expectations</code>
            </td>
            <td>
            </td>
            <td>
              <div class="doc-md-description">
                <p>a dictionary defining the incidence and distribution of expected value
within the population in question.</p>
              </div>
            </td>
            <td>
                  <code>None</code>
            </td>
          </tr>
      </tbody>
    </table>


    <p><span class="doc-section-title">Returns:</span></p>
    <table>
      <thead>
        <tr>
<th>Name</th>          <th>Type</th>
          <th>Description</th>
        </tr>
      </thead>
      <tbody>
          <tr class="doc-section-item">
<td><code>list</code></td>            <td>
            </td>
            <td>
              <div class="doc-md-description">
                <p>of integers of <code>1</code> or <code>0</code> if <code>returning</code> argument is set to <code>binary_flag</code>;
list of strings with a date format returned if <code>returning</code> argument is set to <code>date_of_death</code>
list of strings returned if <code>returning</code> argument is set to <code>underlying_cause_of_death</code> or <code>place_of_death</code></p>
              </div>
            </td>
          </tr>
      </tbody>
    </table>
        <p>Example:</p>
<div class="highlight"><pre><span></span><code>A variable called `died_ons_covid_flag_any` is created that returns the date of death for
any patients that have covid on their death certificate even if that is the not the underlying cause
of death.

    died_ons_covid_flag_any=patients.with_these_codes_on_death_certificate(
        covid_codelist,
        on_or_after=&quot;2020-02-01&quot;,
        match_only_underlying_cause=False,
        return_expectations={
            &quot;date&quot;: {&quot;earliest&quot; : &quot;2020-02-01&quot;},
            &quot;rate&quot; : &quot;exponential_increase&quot;
        },
    )
</code></pre></div>


    </div>

</div>

&nbsp;


## ISARIC
---8<-- 'includes/isaric-warning-header.md'

These variables are derived from data provided by the International Severe Acute Respiratory and Emerging Infection Consortium.

For more information, see the [ISARIC section](../data-sources/isaric.md).
&nbsp;


<div class="doc doc-object doc-function">


<h4 id="cohortextractor.patients.with_an_isaric_record" class="doc doc-heading">
            <code class="highlight language-python"><span class="n">with_an_isaric_record</span><span class="p">(</span><span class="n">returning</span><span class="p">,</span> <span class="n">between</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span> <span class="n">date_filter_column</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span> <span class="n">date_format</span><span class="o">=</span><span class="s1">&#39;YYYY-MM-DD&#39;</span><span class="p">,</span> <span class="n">return_expectations</span><span class="o">=</span><span class="kc">None</span><span class="p">)</span></code>

<a href="#cohortextractor.patients.with_an_isaric_record" class="headerlink" title="Permanent link">🔗</a></h4>


    <div class="doc doc-contents first">

        <p>Return whether patient has an ISARIC record</p>


<p><span class="doc-section-title">Parameters:</span></p>
    <table>
      <thead>
        <tr>
          <th>Name</th>
          <th>Type</th>
          <th>Description</th>
          <th>Default</th>
        </tr>
      </thead>
      <tbody>
          <tr class="doc-section-item">
            <td>
                <code>returning</code>
            </td>
            <td>
            </td>
            <td>
              <div class="doc-md-description">
                <p>the ISARIC table column to return</p>
              </div>
            </td>
            <td>
                <em>required</em>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>between</code>
            </td>
            <td>
            </td>
            <td>
              <div class="doc-md-description">
                <p>two dates of interest as a list with each date as a string with the format <code>YYYY-MM-DD</code>.
Filters results to measurements between the two dates provided (inclusive).
The two dates must be in chronological order.</p>
              </div>
            </td>
            <td>
                  <code>None</code>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>date_filter_column</code>
            </td>
            <td>
            </td>
            <td>
              <div class="doc-md-description">
                <p>the ISARIC column to use with <code>between</code> arg.</p>
              </div>
            </td>
            <td>
                  <code>None</code>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>return_expectations</code>
            </td>
            <td>
            </td>
            <td>
              <div class="doc-md-description">
                <p>as described elsewhere.</p>
              </div>
            </td>
            <td>
                  <code>None</code>
            </td>
          </tr>
      </tbody>
    </table>


    </div>

</div>

&nbsp;


## High Cost Drugs
These variables are derived from the High Cost Drugs data which contains specialist medicines prescribed by hospitals to patients for the management of long term conditions.
For more information, see the [High Cost Drugs section](../data-sources/hcd.md).


<div class="doc doc-object doc-function">


<h4 id="cohortextractor.patients.with_high_cost_drugs" class="doc doc-heading">
            <code class="highlight language-python"><span class="n">with_high_cost_drugs</span><span class="p">(</span><span class="n">drug_name_matches</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span> <span class="n">on_or_before</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span> <span class="n">on_or_after</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span> <span class="n">between</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span> <span class="n">returning</span><span class="o">=</span><span class="s1">&#39;binary_flag&#39;</span><span class="p">,</span> <span class="n">date_format</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span> <span class="n">find_first_match_in_period</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span> <span class="n">find_last_match_in_period</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span> <span class="n">return_expectations</span><span class="o">=</span><span class="kc">None</span><span class="p">)</span></code>

<a href="#cohortextractor.patients.with_high_cost_drugs" class="headerlink" title="Permanent link">🔗</a></h4>


    <div class="doc doc-contents first">

        <p>Returns data from the High Cost Drugs Dataset</p>
<p>More details on this <abbr title="A tabular data structure with one row per patient and one column per variable.">dataset</abbr> available here:
https://wellcomeopenresearch.org/articles/6-360</p>


<p><span class="doc-section-title">Parameters:</span></p>
    <table>
      <thead>
        <tr>
          <th>Name</th>
          <th>Type</th>
          <th>Description</th>
          <th>Default</th>
        </tr>
      </thead>
      <tbody>
          <tr class="doc-section-item">
            <td>
                <code>drug_name_matches</code>
            </td>
            <td>
            </td>
            <td>
              <div class="doc-md-description">
                <p>a drug name as a string, or a list of such names, or
a <abbr title="a collection of clinical codes that define a particular condition, event or diagnosis.">codelist</abbr> containing such names. Results will be filtered to just
rows matching any of the supplied names exactly. Note these are not
standardised names, they are just the names however they come to us
in the original data.</p>
              </div>
            </td>
            <td>
                  <code>None</code>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>returning</code>
            </td>
            <td>
            </td>
            <td>
              <div class="doc-md-description">
                <p>string indicating value to be returned. Options are:</p>
<ul>
<li><code>binary_flag</code>: if the patient received any matching drugs</li>
<li><code>date</code>: date drug received</li>
</ul>
              </div>
            </td>
            <td>
                  <code>&#39;binary_flag&#39;</code>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>on_or_before</code>
            </td>
            <td>
            </td>
            <td>
              <div class="doc-md-description">
                <p>as described elsewhere</p>
              </div>
            </td>
            <td>
                  <code>None</code>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>on_or_after</code>
            </td>
            <td>
            </td>
            <td>
              <div class="doc-md-description">
                <p>as described elsewhere</p>
              </div>
            </td>
            <td>
                  <code>None</code>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>between</code>
            </td>
            <td>
            </td>
            <td>
              <div class="doc-md-description">
                <p>as described elsewhere</p>
              </div>
            </td>
            <td>
                  <code>None</code>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>find_first_match_in_period</code>
            </td>
            <td>
            </td>
            <td>
              <div class="doc-md-description">
                <p>as described elsewhere</p>
              </div>
            </td>
            <td>
                  <code>None</code>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>find_last_match_in_period</code>
            </td>
            <td>
            </td>
            <td>
              <div class="doc-md-description">
                <p>as described elsewhere</p>
              </div>
            </td>
            <td>
                  <code>None</code>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>date_format</code>
            </td>
            <td>
            </td>
            <td>
              <div class="doc-md-description">
                <p>only "YYYY" and "YYYY-MM" supported here as day level data
not available</p>
              </div>
            </td>
            <td>
                  <code>None</code>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>return_expectations</code>
            </td>
            <td>
            </td>
            <td>
              <div class="doc-md-description">
                <p>as described elsewhere</p>
              </div>
            </td>
            <td>
                  <code>None</code>
            </td>
          </tr>
      </tbody>
    </table>


<details class="example" open>
  <summary>Example</summary>
  <p>The first month in which each patient received "ACME Drug" after March
2019:</p>
<div class="highlight"><pre><span></span><code>covid_admission_date=patients.with_high_cost_drugs(
    drug_name_matches=&quot;ACME Drug&quot;,
    on_or_after=&quot;2019-03-01&quot;,
    find_first_match_in_period=True,
    returning=&quot;date&quot;,
    date_format=&quot;YYYY-MM&quot;,
    return_expectations={&quot;date&quot;: {&quot;earliest&quot;: &quot;2019-03-01&quot;}},
)
</code></pre></div>
</details>

    </div>

</div>

&nbsp;


## SUS
These variables are derived from the Secondary Uses Services (SUS) data, and their underlying datasets:

* [APCS](../data-sources/apc.md)
* [ECDS](../data-sources/ecds.md)
* OPA


<div class="doc doc-object doc-function">


<h4 id="cohortextractor.patients.admitted_to_hospital" class="doc doc-heading">
            <code class="highlight language-python"><span class="n">admitted_to_hospital</span><span class="p">(</span><span class="n">on_or_before</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span> <span class="n">on_or_after</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span> <span class="n">between</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span> <span class="n">returning</span><span class="o">=</span><span class="s1">&#39;binary_flag&#39;</span><span class="p">,</span> <span class="n">find_first_match_in_period</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span> <span class="n">find_last_match_in_period</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span> <span class="n">date_format</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span> <span class="n">with_these_diagnoses</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span> <span class="n">with_these_primary_diagnoses</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span> <span class="n">with_these_procedures</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span> <span class="n">with_admission_method</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span> <span class="n">with_source_of_admission</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span> <span class="n">with_discharge_destination</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span> <span class="n">with_patient_classification</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span> <span class="n">with_admission_treatment_function_code</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span> <span class="n">with_administrative_category</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span> <span class="n">with_at_least_one_day_in_critical_care</span><span class="o">=</span><span class="kc">False</span><span class="p">,</span> <span class="n">return_expectations</span><span class="o">=</span><span class="kc">None</span><span class="p">)</span></code>

<a href="#cohortextractor.patients.admitted_to_hospital" class="headerlink" title="Permanent link">🔗</a></h4>


    <div class="doc doc-contents first">

        <p>Return information about admission to hospital.</p>
<p>See https://github.com/opensafely/cohort-extractor/issues/186 for in-depth discussion and background.</p>


<p><span class="doc-section-title">Parameters:</span></p>
    <table>
      <thead>
        <tr>
          <th>Name</th>
          <th>Type</th>
          <th>Description</th>
          <th>Default</th>
        </tr>
      </thead>
      <tbody>
          <tr class="doc-section-item">
            <td>
                <code>on_or_before</code>
            </td>
            <td>
            </td>
            <td>
              <div class="doc-md-description">
                <p>date of interest as a string with the format <code>YYYY-MM-DD</code>. Filters results to
on or before the given date.</p>
              </div>
            </td>
            <td>
                  <code>None</code>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>on_or_after</code>
            </td>
            <td>
            </td>
            <td>
              <div class="doc-md-description">
                <p>date of interest as a string with the format <code>YYYY-MM-DD</code>. Filters results to
on or after the given date.</p>
              </div>
            </td>
            <td>
                  <code>None</code>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>between</code>
            </td>
            <td>
            </td>
            <td>
              <div class="doc-md-description">
                <p>two dates of interest as a list with each date as a string with the format <code>YYYY-MM-DD</code>.
Filters results to between the two dates provided (inclusive). The two dates must be in chronological order.</p>
              </div>
            </td>
            <td>
                  <code>None</code>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>returning</code>
            </td>
            <td>
            </td>
            <td>
              <div class="doc-md-description">
                <p>string indicating value to be returned. Options are:</p>
<ul>
<li><code>binary_flag</code>: if they were admitted at all,</li>
<li><code>date_admitted</code>: date patient admitted to hospital,</li>
<li><code>date_discharged</code>: date patient discharged from hospital,</li>
<li><code>number_of_matches_in_period</code>: number of times patient was admitted in time period specified,</li>
<li><code>primary_diagnosis</code>: primary diagnosis code for admission,</li>
<li><code>admission_method</code>: 2-digit code identifying method of admission: planned (booked/planned/waiting list),
    emergency (various types), transfer from another provider, or birth/maternity.</li>
<li><code>source_of_admission</code>: 2-digit code identifying source of admission: most commonly = <code>19</code> <code>usual place of residence</code>.
    Also useful for identifying admissions from care homes ('54', '65', '85', '88').
    Somewhat useful for identifying birth spells and admissions via transfer (but <code>method_of_admission</code> usually preferable)</li>
<li><code>discharge_destination</code>: ,</li>
<li><code>patient_classification</code>: single-digit numeric code:<ul>
<li><code>1</code> ordinary admission;</li>
<li><code>2</code> day case;</li>
<li><code>3</code>/<code>4</code> regular admissions (e.g. patient admitted weekly for chemotherapy or dialysis);</li>
<li><code>5</code> mother and baby using delivery facilities only.</li>
</ul>
</li>
<li><code>admission_treatment_function_code</code>: specialty of patient admission (use with caution for emergency admissions),</li>
<li><code>days_in_critical_care</code>: number of days in critical care during spell,</li>
<li><code>administrative_category</code>: private vs NHS funded treatment,</li>
<li><code>duration_of_elective_wait</code>: days on waiting list for planned procedures (use with caution).</li>
<li><code>total_bed_days_in_period</code>: total number of bed days for all admissisions during the time period specified.</li>
<li><code>total_critical_care_days_in_period</code>: total number of critical care days for all admissisions during the time period specified.</li>
</ul>
              </div>
            </td>
            <td>
                  <code>&#39;binary_flag&#39;</code>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>find_first_match_in_period</code>
            </td>
            <td>
            </td>
            <td>
              <div class="doc-md-description">
                <p>a boolean that indicates if the data returned is first event
if there are multiple matches within the time period</p>
              </div>
            </td>
            <td>
                  <code>None</code>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>find_last_match_in_period</code>
            </td>
            <td>
            </td>
            <td>
              <div class="doc-md-description">
                <p>a boolean that indicates if the data returned is last event
if there are multiple matches within the time period</p>
              </div>
            </td>
            <td>
                  <code>None</code>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>date_format</code>
            </td>
            <td>
            </td>
            <td>
              <div class="doc-md-description">
                <p>a string detailing the format of the dates to be returned. It can be <code>YYYY-MM-DD</code>,
<code>YYYY-MM</code> or <code>YYYY</code> and wherever possible the least disclosive data should be returned. i.e returning
only year is less disclosive than a date with day, month and year.</p>
              </div>
            </td>
            <td>
                  <code>None</code>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>with_these_diagnoses</code>
            </td>
            <td>
            </td>
            <td>
              <div class="doc-md-description">
                <p>icd10 codes to match against any diagnosis (note
this uses <strong>prefix</strong> matching so a code like <code>J12</code> will match
<code>J120</code>, <code>J121</code> etc.)</p>
              </div>
            </td>
            <td>
                  <code>None</code>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>with_these_primary_diagnoses</code>
            </td>
            <td>
            </td>
            <td>
              <div class="doc-md-description">
                <p>icd10 codes to match against the primary
diagnosis note this uses <strong>prefix</strong> matching so a code like <code>J12</code>
will match <code>J120</code>, <code>J121</code> etc.)</p>
              </div>
            </td>
            <td>
                  <code>None</code>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>with_these_procedures</code>
            </td>
            <td>
            </td>
            <td>
              <div class="doc-md-description">
                <p>opcs4 codes to match against the procedure</p>
              </div>
            </td>
            <td>
                  <code>None</code>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>with_admission_method</code>
            </td>
            <td>
            </td>
            <td>
              <div class="doc-md-description">
                <p>string or list of strings to match against</p>
              </div>
            </td>
            <td>
                  <code>None</code>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>with_source_of_admission</code>
            </td>
            <td>
            </td>
            <td>
              <div class="doc-md-description">
                <p>string or list of strings to match against</p>
              </div>
            </td>
            <td>
                  <code>None</code>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>with_discharge_destination</code>
            </td>
            <td>
            </td>
            <td>
              <div class="doc-md-description">
                <p>string or list of strings to match against</p>
              </div>
            </td>
            <td>
                  <code>None</code>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>with_patient_classification</code>
            </td>
            <td>
            </td>
            <td>
              <div class="doc-md-description">
                <p>string or list of strings to match against</p>
              </div>
            </td>
            <td>
                  <code>None</code>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>with_admission_treatment_function_code</code>
            </td>
            <td>
            </td>
            <td>
              <div class="doc-md-description">
                <p>string or list of strings to match against</p>
              </div>
            </td>
            <td>
                  <code>None</code>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>with_administrative_category</code>
            </td>
            <td>
            </td>
            <td>
              <div class="doc-md-description">
                <p>string or list of strings to match against</p>
              </div>
            </td>
            <td>
                  <code>None</code>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>with_at_least_one_day_in_critical_care</code>
            </td>
            <td>
            </td>
            <td>
              <div class="doc-md-description">
                <p>a boolean; if True, matches only admissions with at
least one critical care day</p>
              </div>
            </td>
            <td>
                  <code>False</code>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>return_expectations</code>
            </td>
            <td>
            </td>
            <td>
              <div class="doc-md-description">
                <p>a dictionary defining the incidence and distribution of expected value
within the population in question.</p>
              </div>
            </td>
            <td>
                  <code>None</code>
            </td>
          </tr>
      </tbody>
    </table>


    <p><span class="doc-section-title">Returns:</span></p>
    <table>
      <thead>
        <tr>
<th>Name</th>          <th>Type</th>
          <th>Description</th>
        </tr>
      </thead>
      <tbody>
          <tr class="doc-section-item">
<td><code>list</code></td>            <td>
            </td>
            <td>
              <div class="doc-md-description">
                <p>of integers of <code>1</code> or <code>0</code> if <code>returning</code> argument is set to <code>binary_flag</code>;
of strings with a date format returned if <code>returning</code> argument is set to <code>date_admitted</code> or <code>date_discharged</code>;
of integers if <code>returning</code> argument is set to <code>number_of_matches_in_period</code>, <code>days_in_critical_care</code> or <code>duration_of_elective_wait</code>;
of strings with alphanumerical code format for ICD10 code if <code>returning</code> argument is set to <code>primary_diagnosis</code>;
of 1-2-digit numeric or alphanumeric codes if <code>returning</code> argument is <code>admission_method</code>, <code>source_of_admission</code>,
<code>discharge_destination</code>, <code>patient_classification</code>, or <code>administrative_category</code>;
of 3-digit numeric specialty codes  if <code>returning</code> argument is <code>admission_treatment_function_code</code></p>
              </div>
            </td>
          </tr>
      </tbody>
    </table>


<details class="example" open>
  <summary>Example</summary>
  <p>The day of each patient's first hospital admission for Covid19:</p>
<div class="highlight"><pre><span></span><code>covid_admission_date=patients.admitted_to_hospital(
    returning= &quot;date_admitted&quot;,
    with_these_diagnoses=covid_codelist,
    on_or_after=&quot;2020-02-01&quot;,
    find_first_match_in_period=True,
    date_format=&quot;YYYY-MM-DD&quot;,
    return_expectations={&quot;date&quot;: {&quot;earliest&quot;: &quot;2020-03-01&quot;}},
)
</code></pre></div>
</details>

    </div>

</div><p>&nbsp;</p>


<div class="doc doc-object doc-function">


<h4 id="cohortextractor.patients.attended_emergency_care" class="doc doc-heading">
            <code class="highlight language-python"><span class="n">attended_emergency_care</span><span class="p">(</span><span class="n">on_or_before</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span> <span class="n">on_or_after</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span> <span class="n">between</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span> <span class="n">returning</span><span class="o">=</span><span class="s1">&#39;binary_flag&#39;</span><span class="p">,</span> <span class="n">find_first_match_in_period</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span> <span class="n">find_last_match_in_period</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span> <span class="n">date_format</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span> <span class="n">with_these_diagnoses</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span> <span class="n">discharged_to</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span> <span class="n">return_expectations</span><span class="o">=</span><span class="kc">None</span><span class="p">)</span></code>

<a href="#cohortextractor.patients.attended_emergency_care" class="headerlink" title="Permanent link">🔗</a></h4>


    <div class="doc doc-contents first">

        <p>Return information about attendance of A&amp;E from the <abbr title="Emergency Care Data Set - the national data set for urgent and emergency care">ECDS</abbr> <abbr title="A tabular data structure with one row per patient and one column per variable.">dataset</abbr>. Please note that there is a limited
number of diagnoses allowed within this <abbr title="A tabular data structure with one row per patient and one column per variable.">dataset</abbr>, and so will not match with the range of diagnoses allowed
in other datasets such as the primary care record.</p>


<p><span class="doc-section-title">Parameters:</span></p>
    <table>
      <thead>
        <tr>
          <th>Name</th>
          <th>Type</th>
          <th>Description</th>
          <th>Default</th>
        </tr>
      </thead>
      <tbody>
          <tr class="doc-section-item">
            <td>
                <code>on_or_before</code>
            </td>
            <td>
            </td>
            <td>
              <div class="doc-md-description">
                <p>date of interest as a string with the format <code>YYYY-MM-DD</code>. Filters results to
on or before the given date.</p>
              </div>
            </td>
            <td>
                  <code>None</code>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>on_or_after</code>
            </td>
            <td>
            </td>
            <td>
              <div class="doc-md-description">
                <p>date of interest as a string with the format <code>YYYY-MM-DD</code>. Filters results to
on or after the given date.</p>
              </div>
            </td>
            <td>
                  <code>None</code>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>between</code>
            </td>
            <td>
            </td>
            <td>
              <div class="doc-md-description">
                <p>two dates of interest as a list with each date as a string with the format <code>YYYY-MM-DD</code>.
Filters results to between the two dates provided (inclusive).
The two dates must be in chronological order.</p>
              </div>
            </td>
            <td>
                  <code>None</code>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>returning</code>
            </td>
            <td>
            </td>
            <td>
              <div class="doc-md-description">
                <p>string indicating value to be returned. Options are:</p>
<ul>
<li><code>binary_flag</code>: Whether patient attended A&amp;E</li>
<li><code>date_arrived</code>: date patient arrived in A&amp;E</li>
<li><code>number_of_matches_in_period</code>: number of times patient attended A&amp;E</li>
<li><code>discharge_destination</code>: <abbr title="SNOMED Clinical Terms, a structured clinical vocabulary for use in an electronic health record, the current standard for coding in the NHS and many jurisdictions globally">SNOMED CT</abbr> code of discharge destination.
   This will be a member of refset 999003011000000105</li>
</ul>
              </div>
            </td>
            <td>
                  <code>&#39;binary_flag&#39;</code>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>find_first_match_in_period</code>
            </td>
            <td>
            </td>
            <td>
              <div class="doc-md-description">
                <p>a boolean that indicates if the data returned is first event
if there are multiple matches within the time period</p>
              </div>
            </td>
            <td>
                  <code>None</code>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>find_last_match_in_period</code>
            </td>
            <td>
            </td>
            <td>
              <div class="doc-md-description">
                <p>a boolean that indicates if the data returned is last event
if there are multiple matches within the time period</p>
              </div>
            </td>
            <td>
                  <code>None</code>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>date_format</code>
            </td>
            <td>
            </td>
            <td>
              <div class="doc-md-description">
                <p>a string detailing the format of the dates to be returned. It can be <code>YYYY-MM-DD</code>,
<code>YYYY-MM</code> or <code>YYYY</code> and wherever possible the least disclosive data should be returned. i.e returning
only year is less disclosive than a date with day, month and year.</p>
              </div>
            </td>
            <td>
                  <code>None</code>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>with_these_diagnoses</code>
            </td>
            <td>
            </td>
            <td>
              <div class="doc-md-description">
                <p>a list of <abbr title="SNOMED Clinical Terms, a structured clinical vocabulary for use in an electronic health record, the current standard for coding in the NHS and many jurisdictions globally">SNOMED CT</abbr> codes</p>
              </div>
            </td>
            <td>
                  <code>None</code>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>discharged_to</code>
            </td>
            <td>
            </td>
            <td>
              <div class="doc-md-description">
                <p>a list of members of refset 999003011000000105.</p>
              </div>
            </td>
            <td>
                  <code>None</code>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>return_expectations</code>
            </td>
            <td>
            </td>
            <td>
              <div class="doc-md-description">
                <p>a dictionary defining the incidence and distribution of expected value
within the population in question.</p>
              </div>
            </td>
            <td>
                  <code>None</code>
            </td>
          </tr>
      </tbody>
    </table>


    <p><span class="doc-section-title">Returns:</span></p>
    <table>
      <thead>
        <tr>
<th>Name</th>          <th>Type</th>
          <th>Description</th>
        </tr>
      </thead>
      <tbody>
          <tr class="doc-section-item">
<td><code>list</code></td>            <td>
            </td>
            <td>
              <div class="doc-md-description">
                <p>of integers of <code>1</code> or <code>0</code> if <code>returning</code> argument is set to <code>binary_flag</code>; list of strings with a
date format returned if <code>returning</code> argument is set to <code>date_arrived</code>; of integers if <code>returning</code>
argument is set to <code>number_of_matches_in_period</code> or <code>discharge_destination</code> (with <abbr title="SNOMED Clinical Terms, a structured clinical vocabulary for use in an electronic health record, the current standard for coding in the NHS and many jurisdictions globally">SNOMED CT</abbr> code as
a numerical value)</p>
              </div>
            </td>
          </tr>
      </tbody>
    </table>
        <p>Example:</p>
<div class="highlight"><pre><span></span><code>A variable called `emergency_care` is created with returns a date of first attendence in A&amp;E if
patient had attended emergency room during the time period.

    emergency_care=patients.attended_emergency_care(
        on_or_after=&quot;2020-01-01&quot;,
        returning=&quot;date_arrived&quot;,
        date_format=&quot;YYYY-MM-DD&quot;,
        find_first_match_in_period=True,
        return_expectations={
            &quot;date&quot;: {&quot;earliest&quot; : &quot;2020-02-01&quot;},
            &quot;rate&quot; : &quot;exponential_increase&quot;
        },
    )
</code></pre></div>


    </div>

</div><p>&nbsp;</p>


<div class="doc doc-object doc-function">


<h4 id="cohortextractor.patients.with_ethnicity_from_sus" class="doc doc-heading">
            <code class="highlight language-python"><span class="n">with_ethnicity_from_sus</span><span class="p">(</span><span class="n">returning</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span> <span class="n">use_most_frequent_code</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span> <span class="n">return_expectations</span><span class="o">=</span><span class="kc">None</span><span class="p">)</span></code>

<a href="#cohortextractor.patients.with_ethnicity_from_sus" class="headerlink" title="Permanent link">🔗</a></h4>


    <div class="doc doc-contents first">

        <p>Returns ethnicity data from the <abbr title="Secondary Uses Service - NHS hospital activity data pseudonymised and used for purposes other than direct care, such as analytics and service planning">SUS</abbr> Datasets</p>


<p><span class="doc-section-title">Parameters:</span></p>
    <table>
      <thead>
        <tr>
          <th>Name</th>
          <th>Type</th>
          <th>Description</th>
          <th>Default</th>
        </tr>
      </thead>
      <tbody>
          <tr class="doc-section-item">
            <td>
                <code>returning</code>
            </td>
            <td>
            </td>
            <td>
              <div class="doc-md-description">
                <p>string indicating value to be returned. Options are:</p>
<ul>
<li><code>code</code>: don't group ethnicities at all, return the recorded code</li>
<li><code>group_6</code>: group ethnicities into 6 groups</li>
<li><code>group_16</code>: group ethnicities into 16 groups</li>
</ul>
              </div>
            </td>
            <td>
                  <code>None</code>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>use_most_frequent_code</code>
            </td>
            <td>
            </td>
            <td>
              <div class="doc-md-description">
                <p>when multiple codes are present, pick the most
frequent one</p>
              </div>
            </td>
            <td>
                  <code>None</code>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>return_expectations</code>
            </td>
            <td>
            </td>
            <td>
              <div class="doc-md-description">
                <p>a dictionary describing what dummy data should
look like</p>
              </div>
            </td>
            <td>
                  <code>None</code>
            </td>
          </tr>
      </tbody>
    </table>


    <p><span class="doc-section-title">Returns:</span></p>
    <table>
      <thead>
        <tr>
<th>Name</th>          <th>Type</th>
          <th>Description</th>
        </tr>
      </thead>
      <tbody>
          <tr class="doc-section-item">
<td><code>list</code></td>            <td>
            </td>
            <td>
              <div class="doc-md-description">
                <p>of integers, encoded (in at least <abbr title="The company behind the SystmOne EHR">TPP</abbr>) in line with 2001 Census categories as follows.</p>
              </div>
            </td>
          </tr>
          <tr class="doc-section-item">
<td></td>            <td>
            </td>
            <td>
              <div class="doc-md-description">
                <p><code>group_6</code>:</p>
              </div>
            </td>
          </tr>
          <tr class="doc-section-item">
<td></td>            <td>
            </td>
            <td>
              <div class="doc-md-description">
                <ul>
<li>1 - White</li>
</ul>
              </div>
            </td>
          </tr>
          <tr class="doc-section-item">
<td></td>            <td>
            </td>
            <td>
              <div class="doc-md-description">
                <ul>
<li>2 - Mixed</li>
</ul>
              </div>
            </td>
          </tr>
          <tr class="doc-section-item">
<td></td>            <td>
            </td>
            <td>
              <div class="doc-md-description">
                <ul>
<li>3 - Asian or Asian British</li>
</ul>
              </div>
            </td>
          </tr>
          <tr class="doc-section-item">
<td></td>            <td>
            </td>
            <td>
              <div class="doc-md-description">
                <ul>
<li>4 - Black or Black British</li>
</ul>
              </div>
            </td>
          </tr>
          <tr class="doc-section-item">
<td></td>            <td>
            </td>
            <td>
              <div class="doc-md-description">
                <ul>
<li>5 - Other Ethnic Groups</li>
</ul>
              </div>
            </td>
          </tr>
          <tr class="doc-section-item">
<td></td>            <td>
            </td>
            <td>
              <div class="doc-md-description">
                <p><code>group_16</code>:</p>
              </div>
            </td>
          </tr>
          <tr class="doc-section-item">
<td></td>            <td>
            </td>
            <td>
              <div class="doc-md-description">
                <ul>
<li>1 - White - British</li>
</ul>
              </div>
            </td>
          </tr>
          <tr class="doc-section-item">
<td></td>            <td>
            </td>
            <td>
              <div class="doc-md-description">
                <ul>
<li>2 - White - Irish</li>
</ul>
              </div>
            </td>
          </tr>
          <tr class="doc-section-item">
<td></td>            <td>
            </td>
            <td>
              <div class="doc-md-description">
                <ul>
<li>3 - White - Any other White background</li>
</ul>
              </div>
            </td>
          </tr>
          <tr class="doc-section-item">
<td></td>            <td>
            </td>
            <td>
              <div class="doc-md-description">
                <ul>
<li>4 - Mixed - White and Black Caribbean</li>
</ul>
              </div>
            </td>
          </tr>
          <tr class="doc-section-item">
<td></td>            <td>
            </td>
            <td>
              <div class="doc-md-description">
                <ul>
<li>5 - Mixed - White and Black African</li>
</ul>
              </div>
            </td>
          </tr>
          <tr class="doc-section-item">
<td></td>            <td>
            </td>
            <td>
              <div class="doc-md-description">
                <ul>
<li>6 - Mixed - White and Asian</li>
</ul>
              </div>
            </td>
          </tr>
          <tr class="doc-section-item">
<td></td>            <td>
            </td>
            <td>
              <div class="doc-md-description">
                <ul>
<li>7 - Mixed - Any other mixed background</li>
</ul>
              </div>
            </td>
          </tr>
          <tr class="doc-section-item">
<td></td>            <td>
            </td>
            <td>
              <div class="doc-md-description">
                <ul>
<li>8 - Asian or Asian British - Indian</li>
</ul>
              </div>
            </td>
          </tr>
          <tr class="doc-section-item">
<td></td>            <td>
            </td>
            <td>
              <div class="doc-md-description">
                <ul>
<li>9 - Asian or Asian British - Pakistani</li>
</ul>
              </div>
            </td>
          </tr>
          <tr class="doc-section-item">
<td></td>            <td>
            </td>
            <td>
              <div class="doc-md-description">
                <ul>
<li>10 - Asian or Asian British - Bangladeshi</li>
</ul>
              </div>
            </td>
          </tr>
          <tr class="doc-section-item">
<td></td>            <td>
            </td>
            <td>
              <div class="doc-md-description">
                <ul>
<li>11 - Asian or Asian British - Any other Asian background</li>
</ul>
              </div>
            </td>
          </tr>
          <tr class="doc-section-item">
<td></td>            <td>
            </td>
            <td>
              <div class="doc-md-description">
                <ul>
<li>12 - Black or Black British - Caribbean</li>
</ul>
              </div>
            </td>
          </tr>
          <tr class="doc-section-item">
<td></td>            <td>
            </td>
            <td>
              <div class="doc-md-description">
                <ul>
<li>13 - Black or Black British - African</li>
</ul>
              </div>
            </td>
          </tr>
          <tr class="doc-section-item">
<td></td>            <td>
            </td>
            <td>
              <div class="doc-md-description">
                <ul>
<li>14 - Black or Black British - Any other Black background</li>
</ul>
              </div>
            </td>
          </tr>
          <tr class="doc-section-item">
<td></td>            <td>
            </td>
            <td>
              <div class="doc-md-description">
                <ul>
<li>15 - Other Ethnic Groups - Chinese</li>
</ul>
              </div>
            </td>
          </tr>
          <tr class="doc-section-item">
<td></td>            <td>
            </td>
            <td>
              <div class="doc-md-description">
                <ul>
<li>16 - Other Ethnic Groups - Any other ethnic group</li>
</ul>
              </div>
            </td>
          </tr>
      </tbody>
    </table>


<details class="example" open>
  <summary>Example</summary>
  <p>Patients with ethnicity, grouped to our 16 categories:</p>
<div class="highlight"><pre><span></span><code>ethnicity_by_16_grouping=patients.with_ethnicity_from_sus(
    returning=&quot;group_16&quot;,
    use_most_frequent_code=True,
)
</code></pre></div>
</details>

    </div>

</div><p>&nbsp;</p>


<div class="doc doc-object doc-function">


<h4 id="cohortextractor.patients.outpatient_appointment_date" class="doc doc-heading">
            <code class="highlight language-python"><span class="n">outpatient_appointment_date</span><span class="p">(</span><span class="n">returning</span><span class="o">=</span><span class="s1">&#39;binary_flag&#39;</span><span class="p">,</span> <span class="n">attended</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span> <span class="n">is_first_attendance</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span> <span class="n">with_these_treatment_function_codes</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span> <span class="n">with_these_procedures</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span> <span class="n">on_or_after</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span> <span class="n">between</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span> <span class="n">date_format</span><span class="o">=</span><span class="s1">&#39;YYYY-MM-DD&#39;</span><span class="p">,</span> <span class="n">find_first_match_in_period</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span> <span class="n">return_expectations</span><span class="o">=</span><span class="kc">None</span><span class="p">)</span></code>

<a href="#cohortextractor.patients.outpatient_appointment_date" class="headerlink" title="Permanent link">🔗</a></h4>


    <div class="doc doc-contents first">

        <p>Return when the patient had an outpatient appointment</p>
<p>Please read and be aware of the <a href="https://github.com/opensafely-core/cohort-extractor/issues/673">known limitations of this data</a></p>
<p>There is also some <a href="https://github.com/opensafely-core/cohort-extractor/issues/492">more in-depth discussion and background</a></p>


<p><span class="doc-section-title">Parameters:</span></p>
    <table>
      <thead>
        <tr>
          <th>Name</th>
          <th>Type</th>
          <th>Description</th>
          <th>Default</th>
        </tr>
      </thead>
      <tbody>
          <tr class="doc-section-item">
            <td>
                <code>returning</code>
            </td>
            <td>
            </td>
            <td>
              <div class="doc-md-description">
                <p>string indicating value to be returned. Options are:</p>
<ul>
<li><code>binary_flag</code>: indicates if they have had an outpatient appointment or not</li>
<li><code>date</code>: latest date of outpatient appointment within the specified period</li>
<li><code>number_of_matches_in_period</code>: number of outpatient appointments in period</li>
<li><code>consultation_medium_used</code>: consultation medium code for the latest outpatient appointment within the specified period (see https://www.datadictionary.nhs.uk/attributes/consultation_medium_used.html?hl=consultation%2Cmedium )</li>
<li><code>find_first_match_in_period</code>: return earliest values for <code>date</code> or <code>consultation_medium_used</code> (instead of latest)</li>
</ul>
              </div>
            </td>
            <td>
                  <code>&#39;binary_flag&#39;</code>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>attended</code>
            </td>
            <td>
            </td>
            <td>
              <div class="doc-md-description">
                <p>if True, filters appointments to only those where the patient
was recorded as being seen. If it is not known whether they attended
(e.g. NULL value), it is assumed that they did not attend.</p>
              </div>
            </td>
            <td>
                  <code>None</code>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>is_first_attendance</code>
            </td>
            <td>
            </td>
            <td>
              <div class="doc-md-description">
                <p>if True, filter appointments to only those where
it is known whether it is a first attendance. If it is not known
(e.g. NULL value), it is assumed that it is not a first attendance.</p>
              </div>
            </td>
            <td>
                  <code>None</code>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>with_these_treatment_function_codes</code>
            </td>
            <td>
            </td>
            <td>
              <div class="doc-md-description">
                <p>Filter the appointments to those
whose "specialty in which the consultant was working during the
period of care" matches the supplied <abbr title="a collection of clinical codes that define a particular condition, event or diagnosis.">codelist</abbr>.</p>
              </div>
            </td>
            <td>
                  <code>None</code>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>with_these_procedures</code>
            </td>
            <td>
            </td>
            <td>
              <div class="doc-md-description">
                <p>Filter the appointments to those whose
<code>Primary_Procedure_Code</code> matches the specified <abbr title="OPCS Classification of Interventions and Procedures version 4: coding system used in NHS hospitals, covering operations, procedures and interventions performed during in-patient stays, day case surgery and some out-patient treatments">OPCS-4</abbr> codes.</p>
              </div>
            </td>
            <td>
                  <code>None</code>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>on_or_after</code>
            </td>
            <td>
            </td>
            <td>
              <div class="doc-md-description">
                <p>date of interest as a string with the format <code>YYYY-MM-DD</code>.
Filters results to on or after the given date. The default value is
<code>None</code>.</p>
              </div>
            </td>
            <td>
                  <code>None</code>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>between</code>
            </td>
            <td>
            </td>
            <td>
              <div class="doc-md-description">
                <p>two dates of interest as a list with each date as a string
with the format <code>YYYY-MM-DD</code>. Filters matches to between the two
dates. The default value is <code>None</code>. The two dates must be in chronological order.</p>
              </div>
            </td>
            <td>
                  <code>None</code>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>date_format</code>
            </td>
            <td>
            </td>
            <td>
              <div class="doc-md-description">
                <p>a string detailing the format of the dates to be returned.
It can be <code>YYYY-MM-DD</code>, <code>YYYY-MM</code> or <code>YYYY</code> and wherever possible
the least disclosive data should be returned. i.e returning only
year is less disclosive than a date with day, month and year.</p>
              </div>
            </td>
            <td>
                  <code>&#39;YYYY-MM-DD&#39;</code>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>return_expectations</code>
            </td>
            <td>
            </td>
            <td>
              <div class="doc-md-description">
                <p>as described elsewhere.</p>
              </div>
            </td>
            <td>
                  <code>None</code>
            </td>
          </tr>
      </tbody>
    </table>


    </div>

</div><p>&nbsp;</p>

## UK Renal Registry
Data on patients under secondary renal care (advanced chronic kidney disease stages 4 and 5, dialysis, and kidney transplantation) are held at the UK Renal Registry (UKRR).


<div class="doc doc-object doc-function">


<h4 id="cohortextractor.patients.with_record_in_ukrr" class="doc doc-heading">
            <code class="highlight language-python"><span class="n">with_record_in_ukrr</span><span class="p">(</span><span class="n">from_dataset</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span> <span class="n">returning</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span> <span class="n">on_or_before</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span> <span class="n">on_or_after</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span> <span class="n">between</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span> <span class="n">date_format</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span> <span class="n">return_expectations</span><span class="o">=</span><span class="kc">None</span><span class="p">)</span></code>

<a href="#cohortextractor.patients.with_record_in_ukrr" class="headerlink" title="Permanent link">🔗</a></h4>


    <div class="doc doc-contents first">

        <p>Return whether patient has a record in the UK Renal Registry</p>


<p><span class="doc-section-title">Parameters:</span></p>
    <table>
      <thead>
        <tr>
          <th>Name</th>
          <th>Type</th>
          <th>Description</th>
          <th>Default</th>
        </tr>
      </thead>
      <tbody>
          <tr class="doc-section-item">
            <td>
                <code>from_dataset</code>
            </td>
            <td>
            </td>
            <td>
              <div class="doc-md-description">
                <p>string value; options are:
* '2019_prevalence' - a prevalence cohort of patients alive and on <abbr title="Renal replacement therapy">RRT</abbr> in December 2019
* '2020_prevalence' - a prevalence cohort of patients alive and on <abbr title="Renal replacement therapy">RRT</abbr> in December 2020
* '2021_prevalence' - a prevalence cohort of patients alive and on <abbr title="Renal replacement therapy">RRT</abbr> in December 2021
* '2020_incidence' - an incidence cohort of patients who started <abbr title="Renal replacement therapy">RRT</abbr> in 2020
* '2020_ckd' - a snapshot prevalence cohort of patient with Stage 4 or 5 <abbr title="Chronic kidney disease">CKD</abbr> who were
    reported to the <abbr title="UK Renal Registry">UKRR</abbr> to be under renal care in December 2020.</p>
              </div>
            </td>
            <td>
                  <code>None</code>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>returning</code>
            </td>
            <td>
            </td>
            <td>
              <div class="doc-md-description">
                <p>string value; options are:
* "binary_flag"
* "renal_centre" - string indicating the code of the main renal centre a
    patient is registered with
* "rrt_start_date" - the latest start date for renal replacement therapy
* "treatment_modality_start" - the treatment modality at <code>rrt_start_date</code> such as
    ICHD, HHD, HD, PD, Tx
* "treatment_modality_prevalence" - the treatment modality from the prevalence data
* "latest_creatinine" - most recent creatinine held by <abbr title="UK Renal Registry">UKRR</abbr>
* "latest_egfr" - most recent eGFR held by <abbr title="UK Renal Registry">UKRR</abbr></p>
              </div>
            </td>
            <td>
                  <code>None</code>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>on_or_before</code>
            </td>
            <td>
            </td>
            <td>
              <div class="doc-md-description">
                <p>date of interest as a string with the format <code>YYYY-MM-DD</code>. Filters results to measurements
on or before the given date.</p>
              </div>
            </td>
            <td>
                  <code>None</code>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>on_or_after</code>
            </td>
            <td>
            </td>
            <td>
              <div class="doc-md-description">
                <p>date of interest as a string with the format <code>YYYY-MM-DD</code>. Filters results to measurements
on or after the given date.</p>
              </div>
            </td>
            <td>
                  <code>None</code>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>between</code>
            </td>
            <td>
            </td>
            <td>
              <div class="doc-md-description">
                <p>two dates of interest as a list with each date as a string with the format <code>YYYY-MM-DD</code>.
Filters results to measurements between the two dates provided (inclusive).
The two dates must be in chronological order.</p>
              </div>
            </td>
            <td>
                  <code>None</code>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>date_format</code>
            </td>
            <td>
            </td>
            <td>
              <div class="doc-md-description">
                <p>a string detailing the format of dates to be returned.
It can be "YYYY-MM-DD", "YYYY-MM" or "YYYY" and wherever possible the least disclosive data should be
returned. i.e returning only year is less disclosive than a date with month and year.</p>
              </div>
            </td>
            <td>
                  <code>None</code>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>return_expectations</code>
            </td>
            <td>
            </td>
            <td>
              <div class="doc-md-description">
                <p>as described elsewhere.</p>
              </div>
            </td>
            <td>
                  <code>None</code>
            </td>
          </tr>
      </tbody>
    </table>


<details class="example" open>
  <summary>Example</summary>
  <p>Return patients who are in the prevalence <abbr title="A tabular data structure with one row per patient and one column per variable.">dataset</abbr> of the <abbr title="UK Renal Registry">UKRR</abbr> in 2019.</p>
<div class="highlight"><pre><span></span><code>ukrr_2019 = patients.with_record_in_ukrr(
    from_dataset=&quot;2019_prevalence&#39;,
    returning=&quot;binary_flag&quot;,
    return_expectations={
        &quot;incidence&quot;: 0.25
    },
)
</code></pre></div>
</details>

    </div>

</div><p>&nbsp;</p>

## NHS England COVID-19 data store
(Documentation on the source of this data will be forthcoming later.)


<div class="doc doc-object doc-function">


<h4 id="cohortextractor.patients.with_healthcare_worker_flag_on_covid_vaccine_record" class="doc doc-heading">
            <code class="highlight language-python"><span class="n">with_healthcare_worker_flag_on_covid_vaccine_record</span><span class="p">(</span><span class="n">returning</span><span class="o">=</span><span class="s1">&#39;binary_flag&#39;</span><span class="p">,</span> <span class="n">return_expectations</span><span class="o">=</span><span class="kc">None</span><span class="p">)</span></code>

<a href="#cohortextractor.patients.with_healthcare_worker_flag_on_covid_vaccine_record" class="headerlink" title="Permanent link">🔗</a></h4>


    <div class="doc doc-contents first">

        <p>Return whether patient was recorded as being a healthcare worker at the
time they received a COVID-19 vaccination.</p>
<p>This data is from the NHS England COVID-19 data store, and reflects
information collected at the point of vaccination where recipients are
asked by vaccination staff whether they are in the category of health and
care worker.</p>


<p><span class="doc-section-title">Parameters:</span></p>
    <table>
      <thead>
        <tr>
          <th>Name</th>
          <th>Type</th>
          <th>Description</th>
          <th>Default</th>
        </tr>
      </thead>
      <tbody>
          <tr class="doc-section-item">
            <td>
                <code>returning</code>
            </td>
            <td>
            </td>
            <td>
              <div class="doc-md-description">
                <p>must be 'binary_flag', if supplied</p>
              </div>
            </td>
            <td>
                  <code>&#39;binary_flag&#39;</code>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>return_expectations</code>
            </td>
            <td>
            </td>
            <td>
              <div class="doc-md-description">
                <p>as described elsewhere.</p>
              </div>
            </td>
            <td>
                  <code>None</code>
            </td>
          </tr>
      </tbody>
    </table>


    </div>


## Therapeutics

These variables are derived from forms submitted by clinicians to NHS England for
patients assessed and approved to receive antivirals/nMABs for COVID-19 in inpatient or outpatient
settings.

For more information, see the [Therapeutics data section](../data-sources/therapeutics.md).
&nbsp;


<div class="doc doc-object doc-function">


<h4 id="cohortextractor.patients.with_covid_therapeutics" class="doc doc-heading">
            <code class="highlight language-python"><span class="n">with_covid_therapeutics</span><span class="p">(</span><span class="n">with_these_statuses</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span> <span class="n">with_these_therapeutics</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span> <span class="n">with_these_indications</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span> <span class="n">on_or_before</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span> <span class="n">on_or_after</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span> <span class="n">between</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span> <span class="n">returning</span><span class="o">=</span><span class="s1">&#39;binary_flag&#39;</span><span class="p">,</span> <span class="n">date_format</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span> <span class="n">find_first_match_in_period</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span> <span class="n">find_last_match_in_period</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span> <span class="n">include_date_of_match</span><span class="o">=</span><span class="kc">False</span><span class="p">,</span> <span class="n">episode_defined_as</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span> <span class="n">return_expectations</span><span class="o">=</span><span class="kc">None</span><span class="p">)</span></code>

<a href="#cohortextractor.patients.with_covid_therapeutics" class="headerlink" title="Permanent link">🔗</a></h4>


    <div class="doc doc-contents first">

        <p>Returns data from the Therapeutics Dataset (<abbr title="The company behind the SystmOne EHR">TPP</abbr> <abbr title="an individual clinical database that a data provider makes accessible via the OpenSAFELY platform.">backend</abbr> only)</p>


<p><span class="doc-section-title">Parameters:</span></p>
    <table>
      <thead>
        <tr>
          <th>Name</th>
          <th>Type</th>
          <th>Description</th>
          <th>Default</th>
        </tr>
      </thead>
      <tbody>
          <tr class="doc-section-item">
            <td>
                <code>with_these_statuses</code>
            </td>
            <td>
            </td>
            <td>
              <div class="doc-md-description">
                <p>a status as a string, or a list of such names. Possible values are
"Approved", "Treatment Complete", "Treatment Not Started", "Treatment Stopped"</p>
              </div>
            </td>
            <td>
                  <code>None</code>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>with_these_therapeutics</code>
            </td>
            <td>
            </td>
            <td>
              <div class="doc-md-description">
                <p>a drug name as a string, or a list of such names, or
a <abbr title="a collection of clinical codes that define a particular condition, event or diagnosis.">codelist</abbr> containing such names. Results will be filtered to just
rows containing any of the supplied names. Note these are not
standardised names, they are just the names however they come to us
in the original data.</p>
              </div>
            </td>
            <td>
                  <code>None</code>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>with_these_indications</code>
            </td>
            <td>
            </td>
            <td>
              <div class="doc-md-description">
                <p>a Covid indication name as a string, or a list
of such names. Possible values are "hospital_onset", "hospitalised_with",
"non_hospitalised"</p>
              </div>
            </td>
            <td>
                  <code>None</code>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>returning</code>
            </td>
            <td>
            </td>
            <td>
              <div class="doc-md-description">
                <p>string indicating value to be returned. Options are:</p>
<ul>
<li><code>binary_flag</code>: if the patient received any matching therapeutic intervention</li>
<li><code>date</code>: date intervention started</li>
<li><code>therapeutic</code>: string of comma-separated drug names</li>
<li><code>risk_group</code>: string of comma-separated risk conditions</li>
<li><code>region</code>: Region recorded for the therapeutic intervention; note this may be different
  to the patient's region</li>
<li><code>number_of_matches_in_period</code></li>
<li><code>number_of_episodes</code></li>
</ul>
              </div>
            </td>
            <td>
                  <code>&#39;binary_flag&#39;</code>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>on_or_before</code>
            </td>
            <td>
            </td>
            <td>
              <div class="doc-md-description">
                <p>as described elsewhere</p>
              </div>
            </td>
            <td>
                  <code>None</code>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>on_or_after</code>
            </td>
            <td>
            </td>
            <td>
              <div class="doc-md-description">
                <p>as described elsewhere</p>
              </div>
            </td>
            <td>
                  <code>None</code>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>between</code>
            </td>
            <td>
            </td>
            <td>
              <div class="doc-md-description">
                <p>as described elsewhere</p>
              </div>
            </td>
            <td>
                  <code>None</code>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>find_first_match_in_period</code>
            </td>
            <td>
            </td>
            <td>
              <div class="doc-md-description">
                <p>as described elsewhere</p>
              </div>
            </td>
            <td>
                  <code>None</code>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>find_last_match_in_period</code>
            </td>
            <td>
            </td>
            <td>
              <div class="doc-md-description">
                <p>as described elsewhere</p>
              </div>
            </td>
            <td>
                  <code>None</code>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>include_date_of_match</code>
            </td>
            <td>
            </td>
            <td>
              <div class="doc-md-description">
                <p>a boolean indicating if an extra column containing the date of the match should be returned.</p>
              </div>
            </td>
            <td>
                  <code>False</code>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>date_format</code>
            </td>
            <td>
            </td>
            <td>
              <div class="doc-md-description">
                <p>a string detailing the format of the treatment dates to be returned.
It can be "YYYY-MM-DD", "YYYY-MM" or "YYYY" and wherever possible the least disclosive data should be
returned. i.e returning only year is less disclosive than a date with month and year.</p>
              </div>
            </td>
            <td>
                  <code>None</code>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>episode_defined_as</code>
            </td>
            <td>
            </td>
            <td>
              <div class="doc-md-description">
                <p>a string expression indicating how an episode should be defined (used when <code>returning</code>="number_of_episodes")</p>
              </div>
            </td>
            <td>
                  <code>None</code>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>return_expectations</code>
            </td>
            <td>
            </td>
            <td>
              <div class="doc-md-description">
                <p>as described elsewhere</p>
              </div>
            </td>
            <td>
                  <code>None</code>
            </td>
          </tr>
      </tbody>
    </table>


<details class="example" open>
  <summary>Example</summary>
  <p>The first date on which non-hospitalised patients had any approved theraputic
after 01 Jan 2022:</p>
<div class="highlight"><pre><span></span><code>covid_therapeutics=patients.with_covid_therapeutics(
    therapeutic_matches=therapeutic_codelist,
    indication_matches=&quot;non-hospitalised&quot;,
    approved=True,
    on_or_after=&quot;2022-01-01&quot;,
    find_first_match_in_period=True,
    returning=&quot;date&quot;,
    date_format=&quot;YYYY-MM-DD&quot;,
    return_expectations={&quot;date&quot;: {&quot;earliest&quot;: &quot;2022-01-01&quot;}},
)
</code></pre></div>
</details>

    </div>

</div><p>&nbsp;</p>

## Utility functions

These variables create new variable from existing variables. They do not extract any data directly.
&nbsp;


<div class="doc doc-object doc-function">


<h4 id="cohortextractor.patients.random_sample" class="doc doc-heading">
            <code class="highlight language-python"><span class="n">random_sample</span><span class="p">(</span><span class="n">percent</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span> <span class="n">return_expectations</span><span class="o">=</span><span class="kc">None</span><span class="p">)</span></code>

<a href="#cohortextractor.patients.random_sample" class="headerlink" title="Permanent link">🔗</a></h4>


    <div class="doc doc-contents first">

        <p>Flags a random sample of approximately <code>percent</code> patients.</p>


<p><span class="doc-section-title">Parameters:</span></p>
    <table>
      <thead>
        <tr>
          <th>Name</th>
          <th>Type</th>
          <th>Description</th>
          <th>Default</th>
        </tr>
      </thead>
      <tbody>
          <tr class="doc-section-item">
            <td>
                <code>percent</code>
            </td>
            <td>
            </td>
            <td>
              <div class="doc-md-description">
                <p>an integer between 1 and 100 for the percent of patients to include within the random sample</p>
              </div>
            </td>
            <td>
                  <code>None</code>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>return_expectations</code>
            </td>
            <td>
            </td>
            <td>
              <div class="doc-md-description">
                <p>a dict containing an expectations definition defining at least an <code>incidence</code></p>
              </div>
            </td>
            <td>
                  <code>None</code>
            </td>
          </tr>
      </tbody>
    </table>


    <p><span class="doc-section-title">Returns:</span></p>
    <table>
      <thead>
        <tr>
<th>Name</th>          <th>Type</th>
          <th>Description</th>
        </tr>
      </thead>
      <tbody>
          <tr class="doc-section-item">
<td><code>list</code></td>            <td>
            </td>
            <td>
              <div class="doc-md-description">
                <p>of integers of <code>1</code> or <code>0</code></p>
              </div>
            </td>
          </tr>
      </tbody>
    </table>


<details class="example" open>
  <summary>Example</summary>
  <p>This creates a variable <code>example</code>, flagging approximately 10% of the population with the value <code>1</code>:</p>
<div class="highlight"><pre><span></span><code>example=patients.random_sample(percent=10, expectations={&#39;incidence&#39;: 0.1})
</code></pre></div>
</details>

    </div>

</div><p>&nbsp;</p>


<div class="doc doc-object doc-function">


<h4 id="cohortextractor.patients.categorised_as" class="doc doc-heading">
            <code class="highlight language-python"><span class="n">categorised_as</span><span class="p">(</span><span class="n">category_definitions</span><span class="p">,</span> <span class="n">return_expectations</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span> <span class="o">**</span><span class="n">extra_columns</span><span class="p">)</span></code>

<a href="#cohortextractor.patients.categorised_as" class="headerlink" title="Permanent link">🔗</a></h4>


    <div class="doc doc-contents first">

        <p>Categorises patients using a set of conditions. Patient's are assigned to the first
condition that they satisfy. Similar to the <code>CASE WHEN</code> function in SQL.</p>


<p><span class="doc-section-title">Parameters:</span></p>
    <table>
      <thead>
        <tr>
          <th>Name</th>
          <th>Type</th>
          <th>Description</th>
          <th>Default</th>
        </tr>
      </thead>
      <tbody>
          <tr class="doc-section-item">
            <td>
                <code>category_definitions</code>
            </td>
            <td>
            </td>
            <td>
              <div class="doc-md-description">
                <p>a dict that defines the condition for each category.
The keys of the dict are strings representing categories. The values are expressions of logic
defining the categories. The variables used in the expressions can be variables defined elsewhere
in the <abbr title="specifies the patients you want to include in your study and defines the variables that describe them. Study definitions are written in a Python script using a human-readable API.">study definition</abbr>, or internal variables that are defined as separate arguments within the
<code>categorised_as</code> call and then discarded. <code>"DEFAULT"</code> is a special condition that catches patients
who do not match any condition, and must be specified.</p>
              </div>
            </td>
            <td>
                <em>required</em>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>return_expectations</code>
            </td>
            <td>
            </td>
            <td>
              <div class="doc-md-description">
                <p>A dict that defined the ratios of each category. The keys are the category values
as strings and the values are ratios as floats. The ratios should add up to 1.</p>
              </div>
            </td>
            <td>
                  <code>None</code>
            </td>
          </tr>
      </tbody>
    </table>


    <p><span class="doc-section-title">Returns:</span></p>
    <table>
      <thead>
        <tr>
<th>Name</th>          <th>Type</th>
          <th>Description</th>
        </tr>
      </thead>
      <tbody>
          <tr class="doc-section-item">
<td><code>list</code></td>            <td>
            </td>
            <td>
              <div class="doc-md-description">
                <p>of strings which each letter representing a category as defined by the algorithm. If the categories
are formatted as <code>"yyyy-mm-dd"</code>, they will be interpreted as dates and can be used as dates elsewhere
in the <abbr title="specifies the patients you want to include in your study and defines the variables that describe them. Study definitions are written in a Python script using a human-readable API.">study definition</abbr>.</p>
              </div>
            </td>
          </tr>
      </tbody>
    </table>
        <p>Example:</p>
<div class="highlight"><pre><span></span><code>This creates a variable of asthma status based on codes for asthma and categorising for recent steroid use.

    current_asthma=patients.categorised_as(
        {
            &quot;1&quot;: &quot;recent_asthma_code AND
                  prednisolone_last_year = 0&quot;
            &quot;2&quot;: &quot;recent_asthma_code AND prednisolone_last_year &gt; 0&quot;
            &quot;0&quot;: &quot;DEFAULT&quot;
        },
        recent_asthma_code=patients.with_these_clinical_events(
            asthma_codes, between=[&quot;2017-02-01&quot;, &quot;2020-01-31&quot;],
        ),
        prednisolone_last_year=patients.with_these_medications(
            pred_codes,
            between=[&quot;2019-02-01&quot;, &quot;2020-01-31&quot;],
            returning=&quot;number_of_matches_in_period&quot;,
        ),
        return_expectations={
            &quot;category&quot;:{&quot;ratios&quot;: {&quot;0&quot;: 0.8, &quot;2&quot;: 0.1, &quot;3&quot;: 0.1}}
        },
    )
</code></pre></div>


    </div>

</div><p>&nbsp;</p>


<div class="doc doc-object doc-function">


<h4 id="cohortextractor.patients.satisfying" class="doc doc-heading">
            <code class="highlight language-python"><span class="n">satisfying</span><span class="p">(</span><span class="n">expression</span><span class="p">,</span> <span class="n">return_expectations</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span> <span class="o">**</span><span class="n">extra_columns</span><span class="p">)</span></code>

<a href="#cohortextractor.patients.satisfying" class="headerlink" title="Permanent link">🔗</a></h4>


    <div class="doc doc-contents first">

        <p>Patients who meet the criteria for one or more expressions. Used as a way of combining groups
or making subgroups based on certain characteristics.</p>


<p><span class="doc-section-title">Parameters:</span></p>
    <table>
      <thead>
        <tr>
          <th>Name</th>
          <th>Type</th>
          <th>Description</th>
          <th>Default</th>
        </tr>
      </thead>
      <tbody>
          <tr class="doc-section-item">
            <td>
                <code>expression</code>
            </td>
            <td>
            </td>
            <td>
              <div class="doc-md-description">
                <p>a string in that links together 2 or more expressions into one statement. key variables
for this expression can be defined under this statement or anywhere in <abbr title="specifies the patients you want to include in your study and defines the variables that describe them. Study definitions are written in a Python script using a human-readable API.">study definition</abbr>.</p>
              </div>
            </td>
            <td>
                <em>required</em>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>return_expectations</code>
            </td>
            <td>
            </td>
            <td>
              <div class="doc-md-description">
                <p>a dictionary defining the rate of expected value
within the population in question</p>
              </div>
            </td>
            <td>
                  <code>None</code>
            </td>
          </tr>
      </tbody>
    </table>


    <p><span class="doc-section-title">Returns:</span></p>
    <table>
      <thead>
        <tr>
<th>Name</th>          <th>Type</th>
          <th>Description</th>
        </tr>
      </thead>
      <tbody>
          <tr class="doc-section-item">
<td><code>list</code></td>            <td>
            </td>
            <td>
              <div class="doc-md-description">
                <p>of integers, either <code>1</code> or <code>0</code></p>
              </div>
            </td>
          </tr>
      </tbody>
    </table>
        <p>Example:</p>
<div class="highlight"><pre><span></span><code>This creates a study population where patients included have asthma and not copd:

    population=patients.satisfying(
        &quot;&quot;&quot;
        has_asthma AND NOT
        has_copd
        &quot;&quot;&quot;,
        has_asthma=patients.with_these_clinical_events(
            asthma_codes, between=[&quot;2017-02-28&quot;, &quot;2020-02-29&quot;],
        ),
        has_copd=patients.with_these_clinical_events(
            copd_codes, between=[&quot;2017-02-28&quot;, &quot;2020-02-29&quot;],
        ),
    )
</code></pre></div>


    </div>

</div><p>&nbsp;</p>


<div class="doc doc-object doc-function">


<h4 id="cohortextractor.patients.date_of" class="doc doc-heading">
            <code class="highlight language-python"><span class="n">date_of</span><span class="p">(</span><span class="n">source</span><span class="p">,</span> <span class="n">date_format</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span> <span class="n">include_month</span><span class="o">=</span><span class="kc">False</span><span class="p">,</span> <span class="n">include_day</span><span class="o">=</span><span class="kc">False</span><span class="p">,</span> <span class="n">return_expectations</span><span class="o">=</span><span class="kc">None</span><span class="p">)</span></code>

<a href="#cohortextractor.patients.date_of" class="headerlink" title="Permanent link">🔗</a></h4>


    <div class="doc doc-contents first">

        <p>Return the date of the event associated with a value in another colum.</p>


<p><span class="doc-section-title">Parameters:</span></p>
    <table>
      <thead>
        <tr>
          <th>Name</th>
          <th>Type</th>
          <th>Description</th>
          <th>Default</th>
        </tr>
      </thead>
      <tbody>
          <tr class="doc-section-item">
            <td>
                <code>source</code>
            </td>
            <td>
            </td>
            <td>
              <div class="doc-md-description">
                <p>name of the column</p>
              </div>
            </td>
            <td>
                <em>required</em>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>date_format</code>
            </td>
            <td>
            </td>
            <td>
              <div class="doc-md-description">
                <p>a string detailing the format of the dates to be returned. It can be <code>YYYY-MM-DD</code>,
<code>YYYY-MM</code> or <code>YYYY</code> and wherever possible the least disclosive data should be returned. i.e returning
only year is less disclosive than a date with day, month and year.</p>
              </div>
            </td>
            <td>
                  <code>None</code>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>return_expectations</code>
            </td>
            <td>
            </td>
            <td>
              <div class="doc-md-description">
                <p>a dictionary defining the incidence and distribution of expected value
within the population in question.</p>
              </div>
            </td>
            <td>
                  <code>None</code>
            </td>
          </tr>
      </tbody>
    </table>
        <p>Example:</p>
<div class="highlight"><pre><span></span><code>Fetch each patient&#39;s latest HbA1c and the date the sample was taken:

    latest_hba1c=patients.with_these_clinical_events(
        hba1c_codes,
        returning=&quot;numeric_value&quot;, find_last_match_in_period=True
    ),
    hba1c_date=patients.date_of(&quot;latest_hba1c&quot;, date_format=&quot;YYYY-MM-DD&quot;),
</code></pre></div>


    </div>

</div><p>&nbsp;</p>


<div class="doc doc-object doc-function">


<h4 id="cohortextractor.patients.minimum_of" class="doc doc-heading">
            <code class="highlight language-python"><span class="n">minimum_of</span><span class="p">(</span><span class="o">*</span><span class="n">column_names</span><span class="p">,</span> <span class="o">**</span><span class="n">extra_columns</span><span class="p">)</span></code>

<a href="#cohortextractor.patients.minimum_of" class="headerlink" title="Permanent link">🔗</a></h4>


    <div class="doc doc-contents first">

        <p>Return the minimum value over the supplied columns e.g</p>
<p>min_value=patients.minimum_of("some_column", "another_column")</p>
<p>Note: this ignores "empty values" (i.e. the values used if there is no data
for a particular column, such as 0.0 for numeric values or the empty string
for dates). This ensures that the minimum of a column with a defined value
and one with a missing value is equal to the defined value.</p>
<p>Additional columns can be defined within the function call which will be
used in computing the minimum but won't themselves appear in the output:</p>
<p>min_value=patients.minimum_of(
      "some_column",
      another_colum=patients.with_these_medications(...)
  )</p>
<p>This function doesn't accept <code>return_expectations</code> but instead derives
dummy values from the values of its source columns.</p>


    </div>

</div><p>&nbsp;</p>


<div class="doc doc-object doc-function">


<h4 id="cohortextractor.patients.maximum_of" class="doc doc-heading">
            <code class="highlight language-python"><span class="n">maximum_of</span><span class="p">(</span><span class="o">*</span><span class="n">column_names</span><span class="p">,</span> <span class="o">**</span><span class="n">extra_columns</span><span class="p">)</span></code>

<a href="#cohortextractor.patients.maximum_of" class="headerlink" title="Permanent link">🔗</a></h4>


    <div class="doc doc-contents first">

        <p>Return the maximum value over the supplied columns e.g</p>
<p>max_value=patients.maximum_of("some_column", "another_column")</p>
<p>Additional columns can be defined within the function call which will be
used in computing the maximum but won't themselves appear in the output:</p>
<p>max_value=patients.maximum_of(
      "some_column",
      another_colum=patients.with_these_medications(...)
  )</p>
<p>This function doesn't accept <code>return_expectations</code> but instead derives
dummy values from the values of its source columns.</p>


    </div>

</div><p>&nbsp;</p>


<div class="doc doc-object doc-function">


<h4 id="cohortextractor.patients.with_value_from_file" class="doc doc-heading">
            <code class="highlight language-python"><span class="n">with_value_from_file</span><span class="p">(</span><span class="n">f_path</span><span class="p">,</span> <span class="n">returning</span><span class="p">,</span> <span class="n">returning_type</span><span class="p">,</span> <span class="n">date_format</span><span class="o">=</span><span class="s1">&#39;YYYY-MM-DD&#39;</span><span class="p">)</span></code>

<a href="#cohortextractor.patients.with_value_from_file" class="headerlink" title="Permanent link">🔗</a></h4>


    <div class="doc doc-contents first">

        <p>Returns values from a file.</p>


<p><span class="doc-section-title">Parameters:</span></p>
    <table>
      <thead>
        <tr>
          <th>Name</th>
          <th>Type</th>
          <th>Description</th>
          <th>Default</th>
        </tr>
      </thead>
      <tbody>
          <tr class="doc-section-item">
            <td>
                <code>f_path</code>
            </td>
            <td>
            </td>
            <td>
              <div class="doc-md-description">
                <p>a string indicating the path to the file. The file must be either a csv or a csv.gz file and must contain a <code>patient_id</code> column.</p>
              </div>
            </td>
            <td>
                <em>required</em>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>returning</code>
            </td>
            <td>
            </td>
            <td>
              <div class="doc-md-description">
                <p>a string indicating the column to return from the file. Whilst the file may contain several columns, only this column will be returned from the file.</p>
              </div>
            </td>
            <td>
                <em>required</em>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>returning_type</code>
            </td>
            <td>
            </td>
            <td>
              <div class="doc-md-description">
                <p>a string indicating the type of the column to return from the file. The options are:
* <code>bool</code>
* <code>date</code>
* <code>str</code>
* <code>int</code>
* <code>float</code></p>
              </div>
            </td>
            <td>
                <em>required</em>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>date_format</code>
            </td>
            <td>
            </td>
            <td>
              <div class="doc-md-description">
                <p>a string indicating the format of the date, if <code>returning_type="date"</code>. The options are:
* <code>YYYY-MM-DD</code> The default value.
* <code>YYYY-MM</code>
* <code>YYYY</code></p>
              </div>
            </td>
            <td>
                  <code>&#39;YYYY-MM-DD&#39;</code>
            </td>
          </tr>
      </tbody>
    </table>
        <p>This function does not accept a <code>return_expectations</code> argument because the file can contain dummy data.</p>


    </div>

</div><p>&nbsp;</p>


<div class="doc doc-object doc-function">


<h4 id="cohortextractor.patients.which_exist_in_file" class="doc doc-heading">
            <code class="highlight language-python"><span class="n">which_exist_in_file</span><span class="p">(</span><span class="n">f_path</span><span class="p">)</span></code>

<a href="#cohortextractor.patients.which_exist_in_file" class="headerlink" title="Permanent link">🔗</a></h4>


    <div class="doc doc-contents first">

        <p>Returns boolean values indicating whether patients exist in a file.</p>


<p><span class="doc-section-title">Parameters:</span></p>
    <table>
      <thead>
        <tr>
          <th>Name</th>
          <th>Type</th>
          <th>Description</th>
          <th>Default</th>
        </tr>
      </thead>
      <tbody>
          <tr class="doc-section-item">
            <td>
                <code>f_path</code>
            </td>
            <td>
            </td>
            <td>
              <div class="doc-md-description">
                <p>a string indicating the path to the file. The file must be either a csv or a csv.gz file and must contain a <code>patient_id</code> column.</p>
              </div>
            </td>
            <td>
                <em>required</em>
            </td>
          </tr>
      </tbody>
    </table>
        <p>This function does not accept a <code>return_expectations</code> argument because the file can contain dummy data.</p>


    </div>

</div>

&nbsp;
