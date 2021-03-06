# saltant

**saltant** at its core is a
[Celery](https://github.com/celery/celery)-powered [Django
app](https://docs.djangoproject.com/en/2.0/ref/applications/) for
running and managing asynchonous tasks with the philosophy that when you
update your task code, you should **never** have to restart your job
queue/workers, or migrate your backend's database. It's a great solution
for an ever-changing code base when downtime is expensive.

## Origin

>  /ˈsæl tnt/
>
> a mutant individual or strain; especially: one produced in a fungal or
> bacterial culture

**saltant** is a mutant strain of
[Tantalus](https://github.com/shahcompbio/tantalus), which served a dual
role as a task runner (just like saltant) and as a genomics
file/metadata database for the [Shah Lab](http://shahlab.ca/) at [BC
Cancer](http://www.bccancer.bc.ca/). The problem with Tantalus was that
tasks needed frequent updating, and that ever-changing server
infrastructure required changes in to the job infrastructure—both of
which usually meant bringing the backend down. And when the backend went
down to sort out task problems, the file/metadata database part had to
go down, too. Hence, there was much to be gained from decoupling the job
system from the file/metadata database system. Hence, saltant.

## Structure

##### \*\*More on this soon\*\*

The [`tasks`](tasks) Django app contains the job system (minus a Celery
instance) and an API. It expects the task scripts and any of its
dependencies to be in [`task_library`](task_library).
