# Postmortem

This project contains tasks for learning about writing a postmortem.

## Tasks To Complete

+ [x] 0. My first postmortem<br/>_**[Blog_Post.md](Blog_Post.md)**_ contains a blog post that meets the following requirements:
  + **INFO:**
    + Using one of the web stack debugging project issue or an outage you have personally face, write a postmortem. Most of you will never have faced an outage, so just get creative and invent your own :)
    + While postmortem format can vary, stick to this one so that you can get properly reviewed by your peers.
  + **Requirements:**
Issue Summary:

Duration: April 10, 2024, 09:00 AM - April 10, 2024, 01:00 PM (UTC)
Impact: The service experienced intermittent downtime, resulting in a degradation of user experience. Approximately 30% of users were affected.
Root Cause: A misconfiguration in the load balancer settings led to an overload on one of the backend servers, causing it to become unresponsive.
Timeline:

09:00 AM: Issue detected through monitoring alerts indicating unusually high latency.
09:10 AM: Enginner noticed increased error rates in application logs.
09:20 AM: Investigation initiated, focusing on backend servers and database connectivity.
09:45 AM: Assumption made that database issues were causing the latency spikes. Database team alerted.
10:15 AM: Database team confirmed no issues on their end. Attention shifted to load balancer and network configurations.
10:45 AM: Load balancer configurations reviewed, revealing a misconfigured setting directing excessive traffic to a single backend server.
11:15 AM: Incident escalated to network engineering team for load balancer reconfiguration.
12:30 PM: Load balancer settings updated to distribute traffic evenly across backend servers.
01:00 PM: Service fully restored, latency back to normal levels.
Root Cause and Resolution:

Root Cause: The root cause of the issue was identified as a misconfiguration in the load balancer settings, causing one backend server to be overloaded with traffic while others remained underutilized.
Resolution: The issue was resolved by reconfiguring the load balancer to evenly distribute traffic across all backend servers, thereby preventing overloads and ensuring system stability.
Corrective and Preventative Measures:

Improvements/Fixes:
Implement automated checks for load balancer configurations to detect anomalies.
Enhance monitoring systems to provide more granular insights into traffic distribution and server performance.
Tasks to Address the Issue:
Update load balancer configurations to enforce traffic distribution policies.
Conduct a thorough review of all network configurations to identify and rectify any other potential misconfigurations.
Schedule regular audits of system configurations to prevent similar incidents in the future.
By implementing these corrective measures and addressing the identified tasks, we aim to enhance the resilience and stability of our system, ensuring uninterrupted service delivery to our users.
