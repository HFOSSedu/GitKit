# Instructor Guide for FarmData2 GitKit

The FarmData2 GitKit repository is a disconnected fork of [FarmData2](https://github.com/DickinsonCollege/FarmData2) created for class activities that introduce Free and Open Source Software (FOSS) collaboration models using git and GitHub with a [forking workflow](https://www.atlassian.com/git/tutorials/
comparing-workflows/forking-workflow).  

## Activities

There is a sequence of 4 activities that cover the following topics:

1. Community and Collaboration: [[Slides](https://github.com/braughtg/GitKitMaterials/raw/main/1-S-CommunityAndCollaboration.pptx) | [Activity](https://github.com/braughtg/GitKitMaterials/raw/main/1-A-CommunityAndCollaboration.docx)]
   * An introduction to FOSS communities, how they collaborate using version control (e.g. git) and repository hosting (e.g. GitHub).
   * Includes practice with the issue tracker, forking and cloning.
2. Working Local & Upstreaming [[Slides](https://github.com/braughtg/GitKitMaterials/raw/main/2-S-WorkingLocallyAndUpstreaming.pptx) | [Activity](https://github.com/braughtg/GitKitMaterials/raw/main/2-A-WorkiongLocallyAndUpstreaming.docx)]
   * Introduces feature branches, commits and pull requests as part of a basic branching workflow.
   * Includes practice with creating and switching branches, staging and committing changes, pushing to origin and submitting pull requests.
3. Staying Synchronized [[Slides](https://github.com/braughtg/GitKitMaterials/raw/main/3-S-StayingSynchronized.pptx) | [Activity](https://github.com/braughtg/GitKitMaterials/raw/main/3-A-StayingSynchronized.docx)]
   * Looks at how asynchronous collaboration results in local repository being out of synch with the upstream and how to resolve this by pulling automatically merged changes.
   * Includes having code merged into upstream main, practice with setting the upstream remote, pulling changes from upstream main, pushing to origin, deleting feature branches.
4. Merge Conflicts [[Slides](https://github.com/braughtg/GitKitMaterials/raw/main/4-S-MergeConflicts.pptx) | [Activity](https://github.com/braughtg/GitKitMaterials/raw/main/4-A-MergeConflicts.docx)]
   * Introduces conflicting changes, how they lead to merge conflicts, how they can be resolved.
   * Includes practice with merging main into a feature branch, merge conflict representation, using a merge tool and updating a pull request.

### Using this Repository

**Note:** One fork will support up to 26 students. If you have more than 26 students you will need to have multiple repositories.

To set up this repository to use in your class, see the [README in .kit](.kit/README.md)

#### Community and Collaboration

In this activity students will fork and clone the repository and will claim a `Round1` issue in the issue tracker.  The activity instructs students to claim an issue by commenting on it and that issues will be assigned to the first student to comment on each issue.  The instructor should assign issues to the student in the issue tracker.  There are enough `Round1` issues for 26 students.

#### Working Local & Upstreaming

In this activity students will make changes to address the issue that they were assigned. They will then make a pull request to the upstream (i.e. your fork).  All of the `Round1` issues have been selected so as not to create any conflicts.  Thus, the students will see that their pull requests can be merged automatically. The pull requests can be merged as they come in, but it has been an effective demonstration to merge them in class when this assignment is complete.

#### Staying Synchronized ####

After the pull requests from the prior assignment have been merged, the `main` branches in the students' local and origin repositories will be out of synch with the upstream `main`.  They will pull the changes from upstream `main` and, if all goes well, they will be fast-forward merged.  They will then push the their local `main` branch, with the updates, to their origin.  This brings the `main` branches of their repositories into synch with the upstream.

After synchronizing with the upstream, the students go on to claim an `Round2` issue in the issue tracker.  There are only 4 `Round2` issues, so multiple students will be working on each one.

At the point when most or all students have synchronized with the upstream, make a pull request for the `addRound2Conflicts` branch in your fork and merge it. This branch creates conflicts with each of the changes requested in a `Round2` issue.  So, when the students ultimately create a pull request for their `Round2` issue it will not be able to be merged automatically.  

It has also been effective to wait to merged the `addRound2Conflicts` branch at the start of the next class meeting. In that case all student will see that their pull request can be merged automatically when they create it.  However, once the `addRound2Conflicts` branch is merged they will all change to not being able to be merged automatically.  Doing this in class allowed for the concurrent changes made by the pull request to be illustrated live.

#### Merge Conflicts

In this activity students synchronize with the upstream to get the conflicting changes that were merged by the `addRound2Conflicts` branch. They then merge those changes into their feature branch creating a conflict.  They use a merge tool to resolve the conflict and then push the changes to their origin to update their pull request.  Their goal is to have their pull requests updated so that they again are able to be merged automatically.  There is ultimately no need to merge these pull requests.

Inevitably some students will be behind on their work and will complete their sync with upstream after you have merged the `addRound2Conflicts` branch.  In these cases, their pull requests will not create a conflict to be resolved.  These students should pull the `mergeConflictPractice` branch and create a pull request for it.  That branch contains conflicts with those introduced in the `addRound2Conflicts` branch.  So they can then complete the activity using the `mergeConflictPractice` branch as it it were their original feature branch. Students not in this situation, but who would like additional practice can also pull and use the `mergeConflictPractice` branch.
